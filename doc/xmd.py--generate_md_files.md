[&#8592; `generate_md_files`](xmd.py--generate_md_files.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `process_doc`](xmd.py--process_doc.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L289)</small>
***

# `generate_md_files`
<small>*Function*</small>  
**Synopsis**

```cpp
generate_md_files(cwd, root, entity)
```

Generate and write out all the files corresponding to an `Entity` and its subentities.

## Parameters
**`cwd`** &#8213; The current working directory, it might be the github repository.  
**`root`** &#8213; The parent `Entity` or `None`.  
**`entity`** &#8213; The entity to generate the markdown files for.  
## Return Value

None.

## Side Effects

Writes to all `md` files that are generated from `entity`.


