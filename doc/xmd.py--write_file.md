[&#8592; `read_file`](xmd.py--read_file.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `deref`](xmd.py--deref.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L269)</small>
***

# `write_file`
<small>*Function* &nbsp; - &nbsp; **file management** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
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


