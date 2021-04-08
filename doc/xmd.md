[&#8593; table](table.md)
***

# xmd
## Overview
0. [Entity](#entity)
1. [ENTITY_WORDS](#entity_words)
2. [SECTION_ORDER](#section_order)
3. [INDENT_WIDTH](#indent_width)
4. [Token](#token)
5. [split_tokens](#split_tokens)
6. [text_slice](#text_slice)
7. [ANCHOR_CHARS](#anchor_chars)
8. [to_md_anchor](#to_md_anchor)
9. [correct_grammar](#correct_grammar)
10. [dedent](#dedent)
11. [parse_block](#parse_block)
12. [parse_group](#parse_group)
13. [parse_xmd](#parse_xmd)
14. [xmd2md](#xmd2md)
15. [process_xmd](#process_xmd)
# Constants
**[`ENTITY_WORDS`](#entity_words)**  
**[`SECTION_ORDER`](#section_order)**  
**[`ANCHOR_CHARS`](#anchor_chars)**  
<small>**parsing**</small>  
**[`INDENT_WIDTH`](#indent_width)**  
# Classes
**[`Entity`](#entity)** &#8213; Source code entity  
<small>**parsing**</small>  
**[`Token`](#token)** &#8213; A token with its position  
# Functions
**[`to_md_anchor`](#to_md_anchor)**  
**[`correct_grammar`](#correct_grammar)**  
**[`xmd2md`](#xmd2md)**  
**[`process_xmd`](#process_xmd)**  
<small>**parsing**</small>  
**[`split_tokens`](#split_tokens)**  
**[`text_slice`](#text_slice)**  
**[`dedent`](#dedent)**  
**[`parse_block`](#parse_block)**  
**[`parse_group`](#parse_group)**  
**[`parse_xmd`](#parse_xmd)**  
# Childs
## `ENTITY_WORDS`

A dictionary containing all entity types, their section title and their signature behavior.

***
## `SECTION_ORDER`

A array containing all entity types and section names



***
## `ANCHOR_CHARS`

These are the characters that are kept in the resulting link to a markdown section,
which is generated out of the title text itself.
Note that spaces are replaced by a hyphen later.


***
## `INDENT_WIDTH`

The expected indent (width in spaces) of the text inside an entity


***
## `Entity`

A named tuple containing information about the entities in the source code


### Attributes
**`type`** &#8213; The type of the entity  
**[`category`](#category)** &#8213; A user defined category  
**`brief`** &#8213; The text that appears in overviews next to the name  
**`display`** &#8213; The displayed title of the entity  
**[`sections`](#sections)** &#8213; Special sections: synopsis, description, return  
**`childs`** &#8213; A list containing all child entities of the entity  
### Childs
#### `category`

It is `None` if it does not belong to any category

##### Example

`@fn[Observers] get`

***
#### `sections`

The synopsis and description sections appear at the top.
The return section appears where retval appears.

***
## `Token`

A token with its position


### Attributes
**`pos`** &#8213; The position in the string it originated from  
**`text`** &#8213; The content of the token  
***
## `to_md_anchor`
**Synopsis**

```cpp
to_md_anchor(txt)
```

Converts the title of a section to the anchor, which can be used in a markdown link.


### Parameter
**`txt`** &#8213; A string containing the title text of the section to generate the anchor for, it should not contain any spaces  
### Return Value

A string that represents the anchor.


***
## `correct_grammar`
**Synopsis**

```cpp
correct_grammar(string, amount)
```

Adjusts the string to the given amount, when the amount is one, all plural letters get removed.
These are identified by "(...)" at the end of string. Otherwise, the parenthesis get removed.


### Parameters
**`string`** &#8213; The string containing parenthesized plural form  
**`amount`** &#8213; The amount to adjust the string to  
### Return Value

The adjusted string


***
## `xmd2md`
**Synopsis**

```cpp
xmd2md(xmd_entity, depth):
```

Creates recursively the markdown text for the xmd_entity and its subentities.


### Parameters
**`xmd_entity`** &#8213; The `Entity` object  
**`depth`** &#8213; The rest depths, in which the subentities are separated into its own files  
### Return Value

A dictionary containing the contents for the markdown files with its relative filename.


***
## `process_xmd`
**Synopsis**

```cpp
process_xmd(xmd_src)
```

Parses xmd source and generates the corresponding markdown code.
It also returns a list of all entities inside.


### Parameter
**`xmd_src`** &#8213; The xmd source  
### Return Values
**`md`** &#8213; The generated markdown text  
**`lst_entities`** &#8213; A list containing all entities  
***
## `split_tokens`
**Synopsis**

```cpp
split_tokens(txt)
```

A function that splits source code into its tokens


### Parameter
**`txt`** &#8213; The source code that should be tokenized  
### Return Value

It returns a list of strings, each of them is a token.


***
## `text_slice`
**Synopsis**

```cpp
text_slice(tokens, index, end=None)
```

Creates slice for extracting the text over the specified range of tokens.


### Parameters
**`tokens`** &#8213; The tokens  
**`index`** &#8213; The first index of the token sequence  
**`end`** &#8213; The first index of the token not in the sequence  
***
## `dedent`
**Synopsis**

```cpp
dedent(line)
```

Tries to dedent a line.


### Parameter
**`line`** &#8213; The line to be dedented  
### Return Value

If it succedes it returns the dedented line, otherwise `None`


***
## `parse_block`
**Synopsis**

```cpp
parse_block(lines)
```

Gets the contents of the next indented block.


### Parameter
**`lines`** &#8213; A list of strings containing all the lines  
### Return Values
**`block`** &#8213; A list of strings containing the dedented lines of the block  
**`rest`** &#8213; A list containing the rest of the lines, that do not belong to the block  
***
## `parse_group`
**Synopsis**

```cpp
parse_group(tokens, start, group)
```

Parse a group that is delimited by group. Nested groups are handled correctly.

### Parameters
**`tokens`** &#8213; A list of tokens  
**`start`** &#8213; The index of the token that is potentially a group delimiter  
**`group`** &#8213; Both delimiting characters  
### Return Values
**`first`** &#8213; The first token inside of the group  
**`last`** &#8213; The first token not inside of the group (could be delimiter)  
**`rest`** &#8213; The first token after the group  
***
## `parse_xmd`
**Synopsis**

```cpp
parse_xmd(xmd_lines)
```

Parses xmd source recursively and collects all subentities and text.


### Parameter
**`xmd_lines`** &#8213; A list of strings containing the lines of the xmd source  
### Return Value

An `Entity` that contains the parsed contents


