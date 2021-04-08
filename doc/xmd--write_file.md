[&#8592; read_file](xmd--read_file.md) | [&#8593; xmd.py](xmd.md) | [&#8594; delete_file](xmd--delete_file.md)
***

# `write_file`
**Synopsis**

```cpp
write_file(fname, s)
```

Write the contents of a string to a text file.
The filename is echoed to `stdout`.

## Parameters
**`fname`** &#8213; The path of the text file.  
**`s`** &#8213; The new contents to be written to the file  
## Return Value

None.

## Side Effects

Writes to the file and generates the directory containing the file, if it does not exist.


