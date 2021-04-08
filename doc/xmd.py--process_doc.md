[&#8592; process_xmd_file](xmd.py--process_xmd_file.md) | [&#8593; xmd.py](xmd.py.md) | [&#8594; read_file](xmd.py--read_file.md)
***

# `process_doc`
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


