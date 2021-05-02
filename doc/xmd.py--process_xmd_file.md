[&#8592; `EntityType`](xmd.py--entitytype.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `process_doc`](xmd.py--process_doc.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L191)</small>
***

# `process_xmd_file`
<small>*Function*</small>  
**Synopsis**

```cpp
process_xmd_file(cwd, o_files, file_index, i_file)
```

Process a single xmd file.

## Parameters
**`cwd`** &#8213; The current working directory, it might be the github repository.  
**`o_files`** &#8213; All output filenames: `[(filename, display, *)...]`.  
**`file_index`** &#8213; The index of the current file in `o_files`.  
**`i_file`** &#8213; The filename of the `xmd` file.  
## Return Value

None.

## Side Effects

Writes to all `md` files that are generated from the `xmd` file named by `i_file`.


