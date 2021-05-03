[&#8592; `entity_has_subfile`](xmd.py--entity_has_subfile.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L233)</small>
***

# `realize_filestructure`
<small>*Function* - **structure**</small>  
**Synopsis**

```cpp
realize_filestructure(xmd_entity : Entity, filename : str, depth=999, section_depth=1)
```

Sets the filename information of the `xmd_entity` and its
subentities recursively.


## Parameters
**`xmd_entity`** &#8213; The root entity.  
**[`filename`](xmd.py--realize_filestructure--filename.md)** &#8213; The expected filename of the generated markdown file to that entity.  
**`depth`** &#8213; The rest depth, in which the subentities are separated into their own files.  
**`section_depth`** &#8213; The depth/count of `#` when creating section headers.  
