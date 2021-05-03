[&#8592; `generate_md_files`](xmd.py--generate_md_files.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `command`](xmd.py--command.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L293)</small>
***

# `process_doc`
<small>*Function*</small>  
**Synopsis**

```cpp
process_doc(cwd)
```

Create the markdown documentation in `doc/` from the `xmd` files in `xdoc/`.

## Parameter
**`cwd`** &#8213; The current working directory, it might be the github repository.  
## Return Value

None.

## Side Effects

Deletes files that existed in the `doc/` directory and writes the new contents of `md` files. If the `doc/` dir does not exist, the directory is created.


