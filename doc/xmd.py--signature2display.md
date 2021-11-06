[&#8592; `text_slice`](xmd.py--text_slice.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `dedent`](xmd.py--dedent.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L156)</small>
***

# `signature2display`
<small>*Function* &nbsp; - &nbsp; **parsing** &nbsp; - &nbsp; ["xmd.py"](../xmd.py)</small>  
**Synopsis**

```python
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


