[&#8592; correct_grammar](xmd--correct_grammar.md) [&#8593; xmd.md](xmd.md) [&#8594; process_xmd](xmd--process_xmd.md)
# `xmd2md`
**Synopsis**

```cpp
xmd2md(xmd_entity, depth)
```

Creates recursively the markdown text for the xmd_entity and its subentities.


## Parameters
**`xmd_entity`** &#8213; The `Entity` object  
**`depth`** &#8213; The rest depths, in which the subentities are separated into its own files  
## Return Value

A dictionary containing the contents for the markdown files with its relative filename.


