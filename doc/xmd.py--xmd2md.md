[&#8592; `generate_browse`](xmd.py--generate_browse.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `split_tokens`](xmd.py--split_tokens.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L250)</small>
***

# `xmd2md`
<small>*Function* - **output**</small>  
**Synopsis**

```cpp
xmd2md(xmd_entity, parent_file, depth=999, section_depth=1)
```

Creates recursively the markdown text for the xmd_entity and its subentities.


## Parameters
**`xmd_entity`** &#8213; The `Entity` object.  
**`parent_file`** &#8213; A tuple identifying the parent file: `(filename, display, *)`.  
**`depth`** &#8213; The rest depth, in which the subentities are separated into their own files.  
**`section_depth`** &#8213; The depth/count of `#` when creating section headers.  
## Return Value

A dictionary containing the contents for the markdown files with its relative filename.


