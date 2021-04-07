[&#8593; table](table.md)
***

# xmd
## Overview
0. [`Entity`](#entity)
1. [`INDENT_WIDTH`](#indent_width)
2. [`split_tokens(txt)`](#split_tokenstxt)

---

## `Entity`
A named tuple containing information about the entities in the source code

### Parameters
**`type`** &#8213; The type of the entity
**`signature`** &#8213; The signature/declaration in the source code
**`display`** &#8213; The displayed title of the entity
**`anchor`** &#8213; The anchor in the markdown files that identifies the entity


---

## `INDENT_WIDTH`
The expected indent (width in spaces) of the text inside an entity


---

## `split_tokens(txt)`
A function that splits source code into its tokens

### Parameters
**`txt`** &#8213; The source code that should be tokenized

### Return value
It returns a list of strings, each of them is a token.


