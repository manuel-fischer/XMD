from collections import namedtuple
import string
import os
import sys

LANG = "cpp"
Entity = namedtuple("Entity", """
    type
    category
    brief
    display
    sections
    childs
""")

EntityType = namedtuple("EntityType", "title inline_brief")

X = EntityType
ENTITY_WORDS = {# Title                  Has inline brief
    "fn":       X("Function(s)",         False),
    "class":    X("Class(es)",           False),
    "struct":   X("Structure(s)",        False),
    "type":     X("Type(s)",             True),
    "const":    X("Constant(s)",         True),
    "var":      X("Variable(s)",         True),
    "def":      X("Macro Definition(s)", False),
    
    "param":    X("Parameter(s)",        True),
    "attr":     X("Attribute(s)",        True),
    "retval":   X("Return Value(s)",     True),
    #"example":  X("Example(s)",          False),
}
SECTION_ORDER = """
    syn
    description
    param
    const
    var
    attr
    return
    retval
    type
    struct
    class
    fn
    def
    example
""".split()
#assert(len(ENTITY_WORDS) == len(ENTITY_ORDER))


SPECIAL_SECTIONS = {
    "syn": "**Synopsis**\n", # if @syn(n), then multiple overloads could be written
                       # if the syntax of a declaration is clear, the entity
                       # itself can be introduced with the syn
    "return": "# Return Value\n",
    "description": "",
    "example":  "# Example",
}


INDENT_WIDTH = 4

Token = namedtuple("Token", "pos text")

def split_tokens(txt):
    tokens = []
    cur_start = 0
    cur_token = ""
    for i, c in enumerate(txt):
        if c in string.whitespace:
            if cur_token:
                tokens.append(Token(cur_start, cur_token))
            cur_start = i+1
            cur_token = ""
        elif c in "()[]{}":
            if cur_token:
                tokens.append(Token(cur_start, cur_token))
            cur_start = i+1
            cur_token = ""
                
            tokens.append(Token(i, c))
        else:
            cur_token += c

    if cur_token:
        tokens.append(Token(cur_start, cur_token))
    return tokens

def text_slice(tokens, index, end=None):
    if index >= len(tokens): return slice(-1,-1)
    else:
        first = tokens[index].pos
        last  = None if end is None or end >= len(tokens) else tokens[end].pos
        return slice(first,last)

ANCHOR_CHARS = set(" -_" + string.ascii_letters + string.digits)
def to_md_anchor(txt):
    return "".join(
        '-' if c == ' ' else c.lower()
        for c in txt
        if c in ANCHOR_CHARS
    )

def to_md_filename_part(name):
    return to_md_anchor(name)

def correct_grammar(string, amount):
    if amount == 1:
        return string[:string.rfind("(")]
    else:
        return string.replace("(","") \
                     .replace(")","")


def signature2display(signature):
    tokens = split_tokens(signature)
    if (i := first_group(tokens)) != None:
        return tokens[i-1].text
    return signature


def entity_has_subfile(entity):
    return bool(entity.childs) \
        or bool("".join(entity.sections.values()).strip())


# Parsing


def dedent(line):
    if line[:1] == '\t': return line[1:]
    if line[:INDENT_WIDTH].replace(" ", "") == "": return line[INDENT_WIDTH:]
    return None

def parse_block(lines):
    block = []
    for l in lines:
        if (d := dedent(l)) is not None:
            block.append(d)
        else:
            break
    return (block, lines[len(block):])

def first_group(tokens, start=0):
    for i in range(start, len(tokens)):
        if tokens[i].text in "()[]{}":
            return i
    return None

def parse_group(tokens, start=0, group="[]"):
    if start < len(tokens) and tokens[start].text == group[0]:
        depth = 0
        for i in range(start+1, len(tokens)):
            if   tokens[i].text == group[1]: depth -= 1
            elif tokens[i].text == group[0]: depth += 1

            if depth == -1: break
        else:
            raise Exception(f"Unmatched {group[0]}")

        return (start+1, i, i+1)            
    else:
        return (start, start, start)

def parse_xmd(xmd_lines, proto, line_no=1):
    (
        type,
        category,
        brief,
        display,
        sections,
        childs
    ) = proto

    if "description" not in sections: sections["description"] = ""

    try:
        while xmd_lines:
            l = xmd_lines[0]
            if l.startswith("@"):
                block, xmd_lines = parse_block(xmd_lines[1:])
                
                ll = l[1:]
                tokens = split_tokens(ll)
                tag = tokens[0].text
                if tag in ENTITY_WORDS:
                    e_type = tag
                    first, last, rest = parse_group(tokens, 1, "[]")
                    e_category = ll[text_slice(tokens, first, last)] if first!=last else ""
     
                    if ENTITY_WORDS[tag].inline_brief:
                        e_signature = e_display = tokens[rest].text
                        e_brief = ll[text_slice(tokens, rest+1)]
                    else:
                        e_signature = ll[text_slice(tokens, rest)]
                        e_display = signature2display(e_signature)
                        e_brief = ""
                    e_sections = {"syn": f"```{LANG}\n{e_signature}\n```"} if e_signature != e_display else {}
                        
                    entity = parse_xmd(
                        block,
                        Entity(
                            type = e_type,
                            category = e_category,
                            brief = e_brief,
                            display = e_display,
                            sections = e_sections,
                            childs = []
                        ),
                        line_no
                    )

                    childs.append(entity)
                else:
                    content = "\n".join([ll[text_slice(tokens, 1)]]+block)
                    if tag == "brief":
                        brief = (brief + " " + content).lstrip()
                    elif tag in SPECIAL_SECTIONS:
                        try:             sections[tag] += content+"\n"
                        except KeyError: sections[tag]  = content+"\n"
                    else:
                        raise Exception(f"Unexpected command {tag}")
                        
            
            else:
                block, xmd_lines = [], xmd_lines[1:]
                # just markdown text, in the description
                sections["description"] += l+"\n"
            line_no += 1+len(block)
    except:
        print(f"Error at line {line_no}")
        raise

    return Entity(
        type,
        category,
        brief,
        display,
        sections,
        childs
    )


DIRECTION_STR = {
    "left":  "&#8592;",
    "up":    "&#8593;",
    "right": "&#8594;",
}

def generate_browse_link(direction, file):
    assert type(file) == tuple
    return f"[{DIRECTION_STR[direction]} {file[1]}]({file[0]})"
    

def generate_browse(parent, files, i):
    return (generate_browse_link("left", files[i-1]) if i != 0 else "") + " " \
         + (generate_browse_link("up", parent)) + " " \
         + (generate_browse_link("right", files[i+1]) if i != len(files)-1 else "") \
         + "\n"


def generate_table(lst_entities, path="", i0=0):
    md = ""
    md += "## Overview\n"
    for i, e in enumerate(lst_entities):
        md += f"{i+i0}. [{e.display}]({path}#{to_md_anchor(e.display)})\n"
    return md


def xmd2md(xmd_entity, parent_file, files, file_index, depth=999, section_depth=1):
    file = files[file_index]
    filename = file[0]
    file_prefix = os.path.splitext(filename)[0]
    
    subfiles = []
    md = ""
    md += generate_browse(parent_file, files, file_index)
    md += section_depth*"#" + f" `{xmd_entity.display}`\n"
    for sect in SECTION_ORDER:
        if sect in ENTITY_WORDS:
            s_childs = [c for c in xmd_entity.childs if c.type == sect]
            s_childs = sorted(s_childs, key=lambda c: c.category or "")

            s_files = [(f"{file_prefix}--{to_md_filename_part(c.display)}.md", c.display) for c in s_childs]
            
            if not s_childs: continue
            section_title = correct_grammar(ENTITY_WORDS[sect].title, len(s_childs))
            md += section_depth*"#" + "# " + section_title + "\n"
            
            cur_category = ""
            for i, c in enumerate(s_childs):
                if c.category != cur_category:
                    md += f"<small>**{c.category}**</small>  \n"
                    cur_category = c.category
                
                has_subfile = entity_has_subfile(c)
                link = f"`{c.display}`"
                kw = dict(parent_file = file, files = s_files, file_index = i)
                if has_subfile:
                    if depth <= 0:
                        subfiles += xmd2md(c, **kw, depth=-1, section_depth=section_depth+2)
                        link = f"[{link}](#{to_md_anchor(c.display)})"
                    else:
                        subfiles += xmd2md(c, **kw, depth=depth-1, section_depth=1)
                        link = f"[{link}]({s_files[i][0]}#{to_md_anchor(c.display)})"
                    
                md += f"**{link}**" # linebreak
                if c.brief:
                    md += f" &#8213; {c.brief}"
                md += "  \n" # two spaces -- linebreak
        else:
            sect_md = xmd_entity.sections.get(sect, "")
            if sect_md:
                section_title = SPECIAL_SECTIONS[sect]
                md += section_title.replace("#", section_depth*"#"+"#") + "\n"
                md += sect_md + "\n"

    if subfiles and depth == 0:
        md += section_depth*"#" + "# " + correct_grammar("Child(s)", len(subfiles)) + "\n"
        first = True
        for e_fn, e_md in subfiles.items():
            if first:
                first = False
            else:
                md += "***\n"
            #md += section_depth*"#" + f"# `{e_fn}`\n"
            md += e_md
            
        subfiles = []

    subfiles += [(filename, xmd_entity.display, md)]
    return subfiles

"""
def process_xmd__(xmd_src):
    entity = parse_xmd(
        xmd_src.split("\n"),
        Entity(
            type = "file",
            category = "",
            brief = "",
            display = "???",
            sections = {},
            childs = []
        )
    )

    md_files = xmd2md(entity, 0)
    assert len(md_files) == 1
    md = md_files["???"]
    return (md, entity.childs)

# return (md, lst_entities)
def process_xmd_(xmd_src):
    xmd = xmd_src
    md = ""
    lst_entities = []

    S_PRE = 0
    S_PARAMS = 1
    S_ATTRS = 2
    S_RETVAL = 3
    S_RETURN = 4
    S_POST = 5

    SUB_ENTITIES = {
        "param": (S_PARAMS, "Parameters"),
        "attr":  (S_ATTRS,  "Attributes"),
        "retval":(S_RETVAL, "Return Values"),
    }

    current_entity = None
    e_state = 0

    
    for i, l in enumerate(xmd.split("\n")):
        if l[:1] == '\t':
            l = ' ' * INDENT_WIDTH + l[1:]
        
        try:
            if current_entity is not None:
                if l[:INDENT_WIDTH].strip() != "":
                    current_entity = None
                    e_state = 0
                else:
                    l = l[INDENT_WIDTH:]
                    if l[:1] == "@":
                        ll = l[1:]
                        tokens = split_tokens(ll)
                        tag = tokens[0].text
                        if tag in SUB_ENTITIES:
                            tag_state, section_title = SUB_ENTITIES[tag]

                            section_title = correct_grammar(ENTITY_WORDS[tag].title, 2)
                            if e_state != tag_state:
                                md += f"### {section_title}\n"
                                e_state = tag_state

                            brief = ll[text_slice(tokens, 2)]
                            
                            md += f"**`{tokens[1].text}`** &#8213; {brief}  \n" # linebreak
                        elif tag == "return":
                            if e_state < S_RETURN:
                                e_state = S_RETURN
                            else:
                                raise Exception("Did not expect return here")
                            
                            md += f"### Return Value\n"
                            md += ll[text_slice(tokens, 1)] + "\n"
                        else:
                            #TODO
                            raise Exception(f"Invalid tag {tag}")
                    else:
                        md += l + '\n'
                    
        
            
            if current_entity is None:
                if not l.startswith("@"):
                    # just markdown text
                    md += l+"\n"

                else:
                    tokens = split_tokens(l)
                    entity_type = tokens[0].text
                    signature = l[text_slice(tokens, 1)]
                    display = f"`{signature}`" # TODO
                    anchor = to_md_anchor(display)

                    current_entity = Entity(
                        type=entity_type,
                        section = None,
                        brief = "",
                        signature = signature,
                        display = display,
                        #anchor = anchor,
                        sections = {},
                        childs = []
                    )
                    lst_entities.append(current_entity)
                    md += "\n---\n\n"
                    md += f"## {display}\n"
        except:
            print(f"Error in line {i+1}")
            raise

    return md, lst_entities
"""

def read_file(fname):
    print(f"Reading {fname}")
    with open(fname, "rt") as f:
        s = f.read()
    return s

def write_file(fname, s):
    print(f"Writing {fname}")
    path = os.path.dirname(fname)
    if not os.path.isdir(path):
        print(f"Create {path}")
        os.makedirs(path, exist_ok=True)
        
    with open(fname, "wt") as f:
        f.write(s)


cwd = sys.argv[1] if len(sys.argv) == 2 else "."


table_ofile = os.path.join(cwd,"doc","table.md")
i_files = os.listdir(os.path.join(cwd, "xdoc"))
o_files = [os.path.splitext(f)[0]+".md" for f in i_files]

for i, f in enumerate(i_files):
    xmd_ifile = os.path.join(cwd,"xdoc",f)
    md_ofile = os.path.join(cwd,"doc",os.path.splitext(f)[0]+".md")
    xmd_src = read_file(xmd_ifile)

    entity = parse_xmd(
        xmd_src.split("\n"),
        Entity(
            type = "file",  
            category = "",
            brief = "",
            display = md_ofile,
            sections = {},
            childs = []
        )
    )

    file_contents = xmd2md(
        entity,
        ("table.md", "table"),
        [(f, f) for f in o_files],
        i,
        depth=999
    )

    for fn, display, md in file_contents:
        write_file(os.path.join(cwd,"doc",fn), md)

"""
for i, f in enumerate(files):
    xmd_ifile = os.path.join(cwd,"xdoc",f)
    md_ofile = os.path.join(cwd,"doc",os.path.splitext(f)[0]+".md")
    xmd = read_file(xmd_ifile)
    md, lst_entities = process_xmd(xmd)

    md = generate_browse("table.md", files, i) \
       + "***\n\n" \
       + f"# {os.path.splitext(f)[0]}\n" \
       + generate_table(lst_entities) \
       + md
    write_file(md_ofile, md)
"""

# file table
md = ""
md += "## Files\n"
for i, f in enumerate(o_files):
    name = os.path.splitext(os.path.split(f)[-1])[0]
    md_link = f
    md += f"{i}. [{name}]({md_link})\n"


write_file(table_ofile, md)
