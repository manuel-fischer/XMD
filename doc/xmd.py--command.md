[&#8592; `process_doc`](xmd.py--process_doc.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `read_file`](xmd.py--read_file.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L81)</small>
***

# `command`
<small>*Function* &nbsp; - &nbsp; **commands** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
@command(name="<name>")
def cmd_<name>(e : entity, content : str):
	...
```


Decorator, that registers a command in `COMMANDS`.

## Parameters
**`name`** &#8213; The name of the command.  
**[`func`](xmd.py--command--func.md)** &#8213; The function that should be registered with the given command name.  
