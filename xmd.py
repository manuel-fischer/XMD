from collections import namedtuple
import string
import os

Entity = namedtuple("Entity", """
    type
    signature
    display
    anchor
""")

INDENT_WIDTH = 4

def split_tokens(txt):
    return txt.split()

def join_tokens(tokens):
    return " ".join(tokens)


ANCHOR_CHARS = set(" -" + string.ascii_letters + string.digits)
def to_md_anchor(txt):
    return "".join(
        '-' if c == ' ' else c.lower()
        for c in txt
        if c in ANCHOR_CHARS
    )

# return (md, lst_entities)
def process_xmd(xmd):
    md = ""
    lst_entities = []

    S_PRE = 0
    S_PARAMS = 1
    S_RETURN = 2
    S_POST = 3

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
                        tokens = split_tokens(l[1:])
                        tag = tokens[0]
                        if tag == "param":
                            if e_state == S_PRE:
                                md += "### Parameters\n"
                                e_state = S_PARAMS
                            elif e_state != S_PARAMS:
                                raise Exception("Did not expect parameter here")
                            
                            md += f"**`{tokens[1]}`** &#8213; {join_tokens(tokens[2:])}\n"
                        elif tag == "return":
                            if e_state < S_RETURN:
                                e_state = S_RETURN
                            else:
                                raise Exception("Did not expect return here")
                            
                            md += f"### Return value\n"
                            md += join_tokens(tokens[1:]) + "\n"
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
                    entity_type = tokens[0]
                    signature = join_tokens(tokens[1:])
                    display = f"`{signature}`" # TODO
                    anchor = to_md_anchor(display)

                    current_entity = Entity(entity_type, signature, display, anchor)
                    lst_entities.append(current_entity)
                    md += "\n---\n\n"
                    md += f"## {display}\n"
        except:
            print(f"Error in line {i+1}")
            raise

    return md, lst_entities

direction_str = {
    "left":  "&#8592;",
    "up":    "&#8593;",
    "right": "&#8594;",
}

def generate_link(direction, file):
    name = os.path.splitext(file)[0]
    return f"[{direction_str[direction]} {name}]({file})"
    

def generate_browse(up, files, i):
    return (generate_link("left", files[i-1]) if i != 0 else "") \
         + (generate_link("up", up)) \
         + (generate_link("right", files[i+1]) if i != len(files)-1 else "") \
         + "\n"


def generate_table(lst_entities, path="", i0=0):
    md = ""
    md += "## Overview\n"
    for i, e in enumerate(lst_entities):
        md += f"{i+i0}. [{e.display}]({path}#{e.anchor})\n"
    return md

def read_file(fname):
    print(f"Reading {fname}")
    with open(fname, "rt") as f:
        s = f.read()
    return s

def write_file(fname, s):
    print(f"Writing {fname}")
    path = os.path.dirname(fname)
    os.makedirs(path, exist_ok=True)
    
    with open(fname, "wt") as f:
        f.write(s)


cwd = "test"


table_ofile = os.path.join(cwd,"doc","table.md")
files = ["main.xmd"]

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

# file table
md = ""
md += "## Files\n"
for i, f in enumerate(files):
    name = os.path.splitext(f)[0]
    md_link = os.path.join(os.path.splitext(f)[0]+".md")
    md += f"{i}. [{name}]({md_link})\n"


write_file(table_ofile, md)
