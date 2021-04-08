[&#8592; dedent](xmd--dedent.md) [&#8593; xmd.md](xmd.md) [&#8594; parse_group](xmd--parse_group.md)
# `parse_block`
**Synopsis**

```cpp
parse_block(lines)
```

Gets the contents of the next indented block.


## Parameter
**`lines`** &#8213; A list of strings containing all the lines  
## Return Values
**`block`** &#8213; A list of strings containing the dedented lines of the block  
**`rest`** &#8213; A list containing the rest of the lines, that do not belong to the block  
