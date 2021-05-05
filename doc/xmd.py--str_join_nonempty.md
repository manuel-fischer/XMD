[&#8592; `parse_xmd`](xmd.py--parse_xmd.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `entity_has_subfile`](xmd.py--entity_has_subfile.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L217)</small>
***

# `str_join_nonempty`
<small>*Function* - **string operations**</small>  
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


