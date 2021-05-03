[&#8592; `Token`](xmd.py--token.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8593; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `EntityType`](xmd.py--entitytype.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd.py.xmd#L24)</small>
***

# `Entity`
<small>*Class* - **structure**</small>  

A named tuple containing information about the entities in the source code.


## Attributes
**`type`** &#8213; The type of the entity.  
**[`category`](xmd.py--entity--category.md)** &#8213; A user defined category.  
**`brief`** &#8213; The text that appears in overviews next to the name.  
**`display`** &#8213; The displayed title of the entity.  
**`sections`** &#8213; The contents of special sections. See SPECIAL_SECTIONS.  
**`childs`** &#8213; A list containing all child entities of the entity.  
**[`location`](xmd.py--entity--location.md)** &#8213; A string that identifies the output filename of the entity  
**`src_location`** &#8213; The input location: `("<filename.xmd>", <line>)`  
**`prev`** &#8213; A weakpointer referring to the previous entity or None. Set by `realize_filestructure`   
**`prev`** &#8213; A weakpointer referring to the next entity or None. Set by `realize_filestructure`  
