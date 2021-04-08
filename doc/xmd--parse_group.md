[&#8592; parse_block](xmd--parse_block.md) | [&#8593; xmd.py](xmd.md) | [&#8594; parse_xmd](xmd--parse_xmd.md)
***

# `parse_group`
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
