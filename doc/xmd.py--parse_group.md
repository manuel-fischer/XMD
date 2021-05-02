[&#8592; `parse_block`](xmd.py--parse_block.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `parse_xmd`](xmd.py--parse_xmd.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L121)</small>
***

# `parse_group`
<small>*Function* - **parsing**</small>  
**Synopsis**

```cpp
parse_group(tokens, start, group)
```

Parse a group that is delimited by group. Nested groups are handled correctly.

## Parameters
**`tokens`** &#8213; A list of tokens.  
**`start`** &#8213; The index of the token that is potentially a group delimiter.  
**`group`** &#8213; Both delimiting characters.  
## Return Values
**`first`** &#8213; The first token inside of the group.  
**`last`** &#8213; The first token not inside of the group (could be delimiter).  
**`rest`** &#8213; The first token after the group.  
