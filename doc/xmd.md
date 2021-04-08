[&#8593; table](table.md)
# `.\doc\xmd.md`
## Constants
**`LANG`** &#8213; The language that is used in generated markdown.  
<small>**markdown**</small>  
**[`ANCHOR_CHARS`](xmd--anchor_chars.md)** &#8213; Characters in a markdown anchor.  
<small>**output**</small>  
**`LONG_LINE`** &#8213; A horizontal line used before brief descriptions.  
**`SPLIT_LINE`** &#8213; A vertical line used in between links of the browse line.  
**`DIRECTION_STR`** &#8213; The arrow characters for all four directions.  
<small>**parsing**</small>  
**`INDENT_WIDTH`** &#8213; The expected indent (width in spaces) of the text inside an entity.  
<small>**structure**</small>  
**`ENTITY_WORDS`** &#8213; A dictionary containing all entity types, their section title and their signature behavior.  
**`SECTION_ORDER`** &#8213; A array containing all entity types and section names.  
**[`SPECIAL_SECTIONS`](xmd--special_sections.md)** &#8213; The names and their section heading of special sections as a dictionary.  
## Classes
<small>**parsing**</small>  
**[`Token`](xmd--token.md)** &#8213; A token with its position.  
<small>**structure**</small>  
**[`Entity`](xmd--entity.md)** &#8213; Source code entity.  
**[`EntityType`](xmd--entitytype.md)** &#8213; The behavior of a source code entity.  
## Functions
<small>**file management**</small>  
**[`read_file`](xmd--read_file.md)** &#8213; Read the contents of a text file.  
**[`write_file`](xmd--write_file.md)** &#8213; Write the contents of a string to a text file.  
**[`delete_file`](xmd--delete_file.md)** &#8213; Delete a (text) file.  
<small>**markdown**</small>  
**[`to_md_anchor`](xmd--to_md_anchor.md)** &#8213; Convert title to markdown anchor.  
**[`to_md_filename_part`](xmd--to_md_filename_part.md)** &#8213; Convert file title to a filename.  
<small>**output**</small>  
**[`correct_grammar`](xmd--correct_grammar.md)** &#8213; Adjusts the string to a given amount.  
**[`generate_browse_link`](xmd--generate_browse_link.md)** &#8213; Generates the correponding link for the browse line.  
**[`generate_browse`](xmd--generate_browse.md)** &#8213; Generates the browse line.  
**[`xmd2md`](xmd--xmd2md.md)**  
<small>**parsing**</small>  
**[`split_tokens`](xmd--split_tokens.md)**  
**[`text_slice`](xmd--text_slice.md)**  
**[`signature2display`](xmd--signature2display.md)** &#8213; Extracts the displayed identifier out of a signature.  
**[`dedent`](xmd--dedent.md)**  
**[`parse_block`](xmd--parse_block.md)**  
**[`parse_group`](xmd--parse_group.md)**  
**[`parse_xmd`](xmd--parse_xmd.md)**  
<small>**string operations**</small>  
**[`str_join_nonempty`](xmd--str_join_nonempty.md)** &#8213; Join strings that are not empty.  
<small>**structure**</small>  
**[`entity_has_subfile`](xmd--entity_has_subfile.md)** &#8213; Checks if the entity has detailed content.  
