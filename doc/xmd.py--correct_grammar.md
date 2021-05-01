[&#8592; `to_md_filename_part`](xmd.py--to_md_filename_part.md) | [&#8593; `xmd.py`](xmd.py.md) | [&#8594; `generate_browse_link`](xmd.py--generate_browse_link.md)
***

# `correct_grammar`
<small>*Function* - **output**</small>  
**Synopsis**

```cpp
correct_grammar(string, amount)
```

Adjusts the string to the given amount, when the amount is one, all plural letters get removed.
These are identified by "(...)" at the end of string. Otherwise, the parenthesis get removed.


## Parameters
**`string`** &#8213; The string containing parenthesized plural form.  
**`amount`** &#8213; The amount to adjust the string to.  
## Return Value

The adjusted string.


