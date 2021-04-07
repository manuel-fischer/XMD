# XMD
Extended markdown for source code documentation.

XMD allows to write documentation for source code, in a markdown like syntax.
The documentation is not written in the source itself, to keep it unpolluted.
To keep the documentation and the source in sync, the script searches through
the sources and checks if any documentation was written for a functions or class (entities).
The output is markdown that can be browsed on the github repository page.

# Usage
`python xmd.py [<repository-path>] [--check-only]`

If `repository-path` is not provided, the current working directory `.` is used.
`--check-only` disables the generation of the output markdown files in the `doc` directory.

# How it works

It goes through the source directories recursively and collects all the files and
all entities in these files. The entities are identified by their signature/declarative part.
These signatures need to appear in the documentation. The signature does not need to be complete
but the tokens of the signature must appear in the same order as in the source.

## detection of a signature
An entity is detected by a signature, a signature either contains one of the signature keywords

**Source Directories**: `src source include`  
These are the directories in which the source files are expected, there is no
distinction between those directories by themselves.

**Source Fileextensions**: `.c .cpp`

**Signature Keywords**: `struct class typedef using #define`


# Syntax of `.xmd` files
```
xmd-file = {text | entity}
entity = "@", entity-type, signature, ["--", display-signature], INDENTED entity-doc
entity-type = "fn" | "class" | "struct" | "type" | "const" | "var" | "def"
entity-doc = {text}
text = {tagged-text | *}
tagged-text = @<tag> [<params>] text
```