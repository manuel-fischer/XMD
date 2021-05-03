[&#8592; XMD Format](xmd-format.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; Table](table.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L1)</small>
***

# `xmd.py`
<small>*File*</small>  
**Synopsis**

```python3 xmd.py [<cwd>]```


## Option
**[`<cwd>`](xmd.py--cwd.md)** &#8213; The current working directory, it might be the github repository.  
## Commands
<small>**commands**</small>  
**`cmd_brief`** &#8213; Implementation for the `@brief` command  
**`cmd_briefx`** &#8213; Implementation for the `@briefx` command  
**`cmd_disp`** &#8213; Implementation for the `@disp` command  
## Constants
**[`LANG`](xmd.py--lang.md)** &#8213; The language that is used in generated markdown.  
<small>**commands**</small>  
**[`COMMANDS`](xmd.py--commands.md)** &#8213; A dictionary mapping from command names to command functions  
<small>**markdown**</small>  
**[`ANCHOR_CHARS`](xmd.py--anchor_chars.md)** &#8213; Characters in a markdown anchor.  
<small>**output**</small>  
**`LONG_LINE`** &#8213; A horizontal line used before brief descriptions.  
**`SPLIT_LINE`** &#8213; A vertical line used in between links of the browse line.  
**`LARGE_SPACE`** &#8213; A string that is inserted where larger spaces should appear.  
**`DIRECTION_STR`** &#8213; The arrow characters for all four directions.  
<small>**parsing**</small>  
**`INDENT_WIDTH`** &#8213; The expected indent (width in spaces) of the text inside an entity.  
<small>**structure**</small>  
**`ENTITY_WORDS`** &#8213; A dictionary containing all entity types, their section title and their signature behavior.  
**`SECTION_ORDER`** &#8213; A array containing all entity types and section names.  
**[`SPECIAL_SECTIONS`](xmd.py--special_sections.md)** &#8213; The names and their section heading of special sections as a dictionary.  
## Type
<small>**implementation details**</small>  
**`wref`** &#8213; Alias for weakref.ref  
## Classes
<small>**parsing**</small>  
**[`Token`](xmd.py--token.md)** &#8213; A token with its position.  
<small>**structure**</small>  
**[`Entity`](xmd.py--entity.md)** &#8213; Source code entity.  
**[`EntityType`](xmd.py--entitytype.md)** &#8213; The behavior of a source code entity.  
## Functions
**[`parse_xmd_file`](xmd.py--parse_xmd_file.md)** &#8213; Parse the `.xmd` file named by `ifile`.  
**[`generate_md_files`](xmd.py--generate_md_files.md)** &#8213; Generate and write out  
**[`generate_md_files`](xmd.py--generate_md_files.md)** &#8213; Generate and write out all the files corresponding to an `Entity` and its subentities.  
**[`process_doc`](xmd.py--process_doc.md)** &#8213; Create the markdown documentation in `doc/` from the `xmd` files in `xdoc/`.  
<small>**commands**</small>  
**[`command`](xmd.py--command.md)** &#8213; Decorator, that registers a command in `COMMANDS`.  
<small>**file management**</small>  
**[`read_file`](xmd.py--read_file.md)** &#8213; Read the contents of a text file.  
**[`write_file`](xmd.py--write_file.md)** &#8213; Write the contents of a string to a text file.  
**[`delete_file`](xmd.py--delete_file.md)** &#8213; Delete a (text) file.  
<small>**implementation details**</small>  
**[`deref`](xmd.py--deref.md)** &#8213; Dereferences a weak reference  
<small>**markdown**</small>  
**[`to_md_anchor`](xmd.py--to_md_anchor.md)** &#8213; Convert title to markdown anchor.  
**[`to_md_filename_part`](xmd.py--to_md_filename_part.md)** &#8213; Convert file title to a filename.  
**[`pack_code`](xmd.py--pack_code.md)** &#8213; Format `code` as a multiline codeblock.  
<small>**output**</small>  
**[`correct_grammar`](xmd.py--correct_grammar.md)** &#8213; Adjusts the string to a given amount.  
**[`generate_browse_link`](xmd.py--generate_browse_link.md)** &#8213; Generates the correponding link for the browse line.  
**[`generate_browse`](xmd.py--generate_browse.md)** &#8213; Generates the browse line.  
**[`xmd2md`](xmd.py--xmd2md.md)**  
<small>**parsing**</small>  
**[`split_tokens`](xmd.py--split_tokens.md)**  
**[`text_slice`](xmd.py--text_slice.md)**  
**[`signature2display`](xmd.py--signature2display.md)** &#8213; Extracts the displayed identifier out of a signature.  
**[`dedent`](xmd.py--dedent.md)**  
**[`parse_block`](xmd.py--parse_block.md)**  
**[`first_group`](xmd.py--first_group.md)** &#8213; Find the next opening or closing grouping token.  
**[`parse_group`](xmd.py--parse_group.md)**  
**[`parse_xmd`](xmd.py--parse_xmd.md)**  
<small>**string operations**</small>  
**[`str_join_nonempty`](xmd.py--str_join_nonempty.md)** &#8213; Join strings that are not empty.  
<small>**structure**</small>  
**[`entity_has_subfile`](xmd.py--entity_has_subfile.md)** &#8213; Checks if the entity has detailed content.  
**[`realize_filestructure`](xmd.py--realize_filestructure.md)** &#8213; Sets the filename information of the `xmd_entity` and its
subentities recursively.  
## TODO


* `@syn` command should strip empty lines at the beginning and end
* A way to force that an entity is inlined in the current entity


