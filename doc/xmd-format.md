[&#8593; Table](table.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[&#8594; `xmd.py`](xmd.py.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<small>[\* xdoc](../xdoc/xmd-format.xmd#L1)</small>
***

# XMD Format
<small>*Topic*</small>  


A `xmd` file consists of markdown text mixed with entities and other tags.

## Syntax
```
file = {tag | markdown}
markdown = ANYTHING
tag = "@", ["@"], (entity | command), signature, indented-block 
```

A double `@@` is self referring to the current layer and allows to override the current entity.


## Commands
**[`syn`](xmd-format--syn.md)** &#8213; Synopsis.  
**`return`** &#8213; Description about the returned value of a function  
**`sidefx`** &#8213; Description about the side effects of a function  
**`example`** &#8213; An example showing the usage of the entity  
**`brief`** &#8213; The brief description of an entity, that is shown in the overview of the parent entity  
**`briefx`** &#8213; Like `@brief` but also adds the text to the description of the entity.  
**`disp`** &#8213; Sets the display name of the entity  
**[`config`](xmd-format--config.md)** &#8213; Set special flags  
**`locate`** &#8213; Set the (header) file location  
**`default`** &#8213; Specifies the default value of the entity  
**[`todo`](xmd-format--todo.md)** &#8213; TODO-Tasks  
**[`see`](xmd-format--see.md)** &#8213; See also  
**`pre`** &#8213; Preconditions  
**`post`** &#8213; Postconditions  
**`note`** &#8213; Notes and hints  
## Tags
<small>**entities**</small>  
**[`topic`](xmd-format--topic.md)** &#8213; Topic  
**`file`** &#8213; File  
**`directory`** &#8213; Directory  
**`module`** &#8213; Module  
**`namespace`** &#8213; Namespace  
**`fn`** &#8213; Function or method  
**`class`** &#8213; Class  
**`struct`** &#8213; Structures  
**`type`** &#8213; Types, type aliases  
**`const`** &#8213; Constant  
**`var`** &#8213; Variable  
**`def`** &#8213; Macro definition  
**`param`** &#8213; Parameter  
**`attr`** &#8213; Attribute  
**`retval`** &#8213; Named return value  
**`cmd`** &#8213; Command  
**`tag`** &#8213; Tag  
**`opt`** &#8213; Command line option or settings option  
**`elem`** &#8213; Element  
