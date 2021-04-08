[&#8592; parse_xmd](xmd--parse_xmd.md) | [&#8593; xmd.md](xmd.md) | [&#8594; entity_has_subfile](xmd--entity_has_subfile.md)
***

# `str_join_nonempty`
**Synopsis**

```cpp
str_join_nonempty(join_string, l)
```

Join strings that are not empty.

## Parameters
**`join_string`** &#8213; The string between the nonempty strings.  
**`l`** &#8213; An iterable of all the strings to be joined.  
## Return Value

The joined string. If an empty string appears between other ones, `join_string` is only inserted once.


