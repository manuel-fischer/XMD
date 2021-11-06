[&#8592; `pack_code`](xmd.py--pack_code.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `generate_browse_link`](xmd.py--generate_browse_link.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L146)</small>
***

# `correct_grammar`
<small>*Function* &nbsp; - &nbsp; **output** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
correct_grammar(string, amount)
```

Adjusts the string to the given amount, when the amount is one, all plural letters get removed.
These are identified by "(...)" at the end of string. Otherwise, the parenthesis get removed.


## Parameters
**`string`** &#8213; The string containing parenthesized plural form.  
**`amount`** &#8213; The amount to adjust the string to.  
## Return Value

The adjusted string.


