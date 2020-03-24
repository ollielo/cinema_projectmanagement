# File-based Composable Image Set format specification

|    |    |
|----|----|
| Date    | 27 Feb 2020 |
| Version | 1.0 |
| Type    | COMPOSABLE_IMAGE_SET |
| Storage | FILES | 
| Extension | `.cis` |

A `composable image set` can be stored as a set of files on disk.

1. A `<name>` is any string of ASCII characters not containing a slash `/` or a dot `.`.
2. Where they do not clash with the specification, additional attributes, groups and datasets may be added by other applications or extensions to this specification.
 

A file-based `.cis` dataset shall have the following structure:

```
cisdata.cis/
    attributes.json (file, required)
        {
            "classname"   : "COMPOSABLE_IMAGE_SET",
            "dims"        : [1024, 768],
            "flags"       : ["IMAGES_INDEPENDENT"],
            "version"     : "1.0",
            "origin"      : "UL" 
        }
    parametertable/ (directory, optional)
        data.csv (file, required) (a CSV file following the Cinema specification)
    variables/ (directory, optional)
        variables.json (file, required)
            {
                "variable_name" : {
                    "type" : "TYPE_STRING",
                    "min"  : "0.0",
                    "max"  : "101.0"
                }
            }
    colormaps/ (directory, optional)
        colormap.xml (colormap file, at least one xml or linkfile required)
        greyscale.json (link file)
            {
                "URL" : "https://whatever/something.xml"
            }
    image/ (directory, required)
        <name>/ (one or more directories, each of which is an image) (required)
            layer/ (directory, required)
                NOTE: no non-layer directories below this level
                <name>/ (required. one or more directories, each of which is a layer)
                    attributes.json (file, optional)
                        {
                            "offset" : [int, int], (defaults to 0,0 if not present)
                            "dims"   : [int, int]  (defaults to 0,0 if not present)
                        }
                    channel/ (directory, required)
                        NOTE: no non-channel directories below this level
                        alpha/  (directory, optional)
                            attribute.json (file, optional) (if not present, type is float)
                                {
                                    "type" : "TYPE_STRING"
                                }
                            data.Z (file, required) (a compressed file of type "type")    
                        depth/  (directory, optional)
                            attribute.json (file, optional) (if not present, type is float)
                                {
                                    "type" : "TYPE_STRING"
                                }
                            data.Z (file, required) (a compressed file of type "type")    
                        lighting/ (directory, optional)
                            attribute.json (file, optional) (if not present, type is float)
                                {
                                    "type" : "TYPE_STRING"
                                }
                            data.Z (file, required) (a compressed file of type "type")    
                        <name>/ (one or more directories, required)
                            attribute.json (file, required)
                                {
                                    "variable" : "name of variable this refers to. must be present in this dataset"
                                }
                            data.Z (file, required) (a compressed file of type "type")    
```
