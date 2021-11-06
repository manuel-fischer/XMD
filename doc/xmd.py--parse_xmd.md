[&#8592; `parse_group`](xmd.py--parse_group.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `str_join_nonempty`](xmd.py--str_join_nonempty.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L207)</small>
***

# `parse_xmd`
<small>*Function* &nbsp; - &nbsp; **parsing** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
parse_xmd(xmd_lines, e : Entity, line_no=1)
```

Parses xmd source recursively and collects all subentities and text.


## Parameters
**`xmd_lines`** &#8213; A list of strings containing the lines of the xmd source.  
**`e`** &#8213; The entity with initial information.  
**`line_no`** &#8213; The line number of the first line of the entity.  
## Return Value

An `Entity` that contains the parsed contents.


