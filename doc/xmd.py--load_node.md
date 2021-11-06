[&#8592; `generate_md_files`](xmd.py--generate_md_files.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `process_doc`](xmd.py--process_doc.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L294)</small>
***

# `load_node`
<small>*Function* &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
load_node(cwd, p, is_root=False)
```

Generate an entity for the directory `p`
If there is an xmd-file with the same name as `p`, the file is used for the root `Entity`.
The files in the directory are inserted as additional childs

## Parameters
**`cwd`** &#8213; The current working directory, it might be the github repository.  
**`p`** &#8213; The directory, for which the `Entity` should be generated  
**`is_root`** &#8213; Set to true for the root folder `doc/`  
## Return Value

The root `Entity`


