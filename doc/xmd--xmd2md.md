[&#8592; generate_browse](xmd--generate_browse.md) | [&#8593; xmd.md](xmd.md) | [&#8594; split_tokens](xmd--split_tokens.md)
***

# `xmd2md`
**Synopsis**

```cpp
xmd2md(xmd_entity, parent_file, files, file_index, depth=999, section_depth=1)
```

Creates recursively the markdown text for the xmd_entity and its subentities.


## Parameters
**`xmd_entity`** &#8213; The `Entity` object.  
**`parent_file`** &#8213; A tuple identifying the parent file: `(filename, display, *)`.  
**`files`** &#8213; A list of file tuples in the current level of the hierarchy: `[(filename, display, *)...]`.  
**`file_index`** &#8213; The index of the current file in `files`.  
**`depth`** &#8213; The rest depths, in which the subentities are separated into its own files.  
**`section_depth`** &#8213; The depth/count of `#` when creating section headers.  
## Return Value

A dictionary containing the contents for the markdown files with its relative filename.


