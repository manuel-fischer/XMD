[&#8592; to_md_anchor](xmd--to_md_anchor.md) | [&#8593; xmd.md](xmd.md) | [&#8594; xmd2md](xmd--xmd2md.md)
# `correct_grammar`
**Synopsis**

```cpp
correct_grammar(string, amount)
```

Adjusts the string to the given amount, when the amount is one, all plural letters get removed.
These are identified by "(...)" at the end of string. Otherwise, the parenthesis get removed.


## Parameters
**`string`** &#8213; The string containing parenthesized plural form  
**`amount`** &#8213; The amount to adjust the string to  
## Return Value

The adjusted string


