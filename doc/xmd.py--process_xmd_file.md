[&#8593; xmd.py](xmd.py.md) | [&#8594; process_doc](xmd.py--process_doc.md)
***

# `process_xmd_file`
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


