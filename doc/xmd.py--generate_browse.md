[&#8592; generate_browse_link](xmd.py--generate_browse_link.md) | [&#8593; xmd.py](xmd.py.md) | [&#8594; xmd2md](xmd.py--xmd2md.md)
***

# `generate_browse`
**Synopsis**

```cpp
generate_browse(parent, files, i)
```

Generates the browse line.

## Parameters
**`parent`** &#8213; A tuple identifying the parent file: `(filename, display, *)`.  
**`files`** &#8213; A list of file tuples in the current level of the hierarchy: `[(filename, display, *)...]`.  
**`i`** &#8213; The index of the current file in `files`.  
