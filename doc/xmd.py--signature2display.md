[&#8592; `text_slice`](xmd.py--text_slice.md) | [&#8593; `xmd.py`](xmd.py.md) | [&#8594; `dedent`](xmd.py--dedent.md)
***

# `signature2display`
<small>*Function* - **parsing**</small>  
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


