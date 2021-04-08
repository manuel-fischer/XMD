[&#8592; dedent](xmd.py--dedent.md) | [&#8593; xmd.py](xmd.py.md) | [&#8594; parse_group](xmd.py--parse_group.md)
***

# `parse_block`
**Synopsis**

```cpp
parse_block(lines)
```

Gets the contents of the next indented block.


## Parameter
**`lines`** &#8213; A list of strings containing all the lines.  
## Return Values
**`block`** &#8213; A list of strings containing the dedented lines of the block.  
**`rest`** &#8213; A list containing the rest of the lines, that do not belong to the block.  
