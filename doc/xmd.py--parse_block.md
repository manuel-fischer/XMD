[&#8592; `dedent`](xmd.py--dedent.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `first_group`](xmd.py--first_group.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L179)</small>
***

# `parse_block`
<small>*Function* &nbsp; - &nbsp; **parsing** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
parse_block(lines)
```

Gets the contents of the next indented block.


## Parameter
**`lines`** &#8213; A list of strings containing all the lines.  
## Return Values
**`block`** &#8213; A list of strings containing the dedented lines of the block.  
**`rest`** &#8213; A list containing the rest of the lines, that do not belong to the block.  
