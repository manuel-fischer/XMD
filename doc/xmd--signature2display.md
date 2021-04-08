[&#8592; text_slice](xmd--text_slice.md) | [&#8593; xmd.py](xmd.md) | [&#8594; dedent](xmd--dedent.md)
***

# `signature2display`
**Synopsis**

```cpp
signature2display(signature)
```

Extracts the displayed identifier out of a signature.

## Parameter
**`signature`** &#8213; The signature as a string.  
## Return Value

the identifier.

## Example

```python
>>> signature2display("int main(int argc, char* argv[])")
'main'
```


