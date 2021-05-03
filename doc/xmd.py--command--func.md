[&#8593; `command`](xmd.py--command.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L78)</small>
***

# `func`
<small>*Parameter*</small>  
**Synopsis**

```cpp
cmd_<name>(e : entity, content : str)
```


The function that should be registered with the given command name.

## Parameters
**`e`** &#8213; The current entity (the context) on which the command is applied to.  
**`content`** &#8213; The contents of the command, might be multiple lines if
the introducing line is followed by indented lines.  
## Return Value

The return value is discarded.



