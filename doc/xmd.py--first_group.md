[&#8592; `parse_block`](xmd.py--parse_block.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `parse_group`](xmd.py--parse_group.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L187)</small>
***

# `first_group`
<small>*Function* &nbsp; - &nbsp; **parsing** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
first_group(tokens, start=0)
```

Find the next opening or closing grouping token.

## Parameters
**`tokens`** &#8213; A list of `Token`s.  
**`start`** &#8213; The starting postion of the search.  
## Return Value

Index of the first token that is a grouping token,
if no grouping token is found return `None`.



