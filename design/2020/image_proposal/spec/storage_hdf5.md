# HDF5 Composable Image Set format specification

|    |    |
|----|----|
| Date    | 10 Dec 2019 |
| Version | 1.0 |
| Type    | COMPOSABLE_IMAGE_SET |
| Extension | `.cis` |
| Authors | David H. Rogers, John Patchet, Ethan Stam, Dave DeMarle, Sebastian Jourdain, Jonas Lucasczyk |

A `composable image set` can be stored a single [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) file. We note the [existing specification](https://support.hdfgroup.org/HDF5/doc/ADGuide/ImageSpec.html) for images to be stored in HDF5 format. Where possible, this specification adopts conventions from that specification. 

If it is stored in HDF5 format, it shall have the following structure, with the following overall restrictions:

1. A `<name>` is any string of ASCII characters not containing a slash `/` or a dot `.`.
2. Where they do not clash with the specification, additional attributes, groups and datasets may be added by other applications or extensions to this specification, but they are ignored by this specification.
 

```
/
    class   (attribute, required) COMPOSABLE_IMAGE_SET 
    dims    (attribute, required) [int, int]
            This is the absolute size of the completed image
    flags   (attribute, optional)
            A list of flags, providing additional information about this data
            - IMAGES_INDEPENDENT images DO NOT have the same set of layers and channels. 
                                 Default, if this flag is not included, is that all images 
                                 have the same layers, and all layers have the same channels.
    version (attribute, required) string
            The version of this specification that the data conforms with
    origin  (attribute, optional) [UL, UR, LL, LR]
            The 0,0 point for the image. Default value is UL
    parametertable/ (group, optional)
                    A table encoding paramter/image/layer relationships for this file
        colnames (attribute, required, comma separated string of all column names)
        num_rows (attribute, required, number of rows (int) )
        columns/ (group, required)
            NOTE: no non-column groups allowed below this level; groups assumed to be columns 
            <int> (dataset of ascii encoded string values, one for each colname.
                  The name of the dataset is a zero-based index that maps to the colnames
                  data above. The values in this dataset can include null strings and the 
                  value "NaN" for NaN as needed)
    variables/ (group, optional)
               Information about the variables encoded in image layers
        NOTE: no non-variable groups allowed below this level; groups assumed to be variables 
        <name>/ (group, at least one required if this group is present)
            type (attribute, required)
            min (attribute, required)
            max (attribute, required)
    colormaps/ (group, optional)
        <name>/ (group, at least one required)
        	space (attribute, required) RGB
            colormap (dataset, required) array of 5D points [x, o, r, g, b]
    image/ (group, required)
        NOTE: no non-image groups allowed below this level; groups assumed to be images 
        <name>/ (one or more named groups, each of which is an image) (required)
            layer/ (group, required)
                NOTE: no non-layer groups allowed below this level; groups assumed to be layers 
                <name>/ (required. one or more named groups, each of which is a layer)
                    offset (attribute, optional) [int, int]
                           Offset of the layer's channels from "/origin". If not included, default
                           value is [0, 0], or no offset
                    dims   (attribute, optional) [int, int]
                           Dimensions of the layer. If not present, assumed to be "/dims"
                    channel/ (group, required)
                        NOTE: no non-channel groups allowed below this level; groups assumed to be channels 
                        depth/  (dataset, optional)
                            type (attribute) (optional) [valid type string]
                                 If not present, values are assumed to be float
                        lighting/ (dataset, optional)
                            type (attribute, optional) [valid type string]
                                 If not present, values are assumed to be float
                        <name>/ (one or more named datasets, required)
                            type (attribute, optional) [valid type string]
                                 If not present, values are assumed to be float
                            variable (attribute, optional)
                                 The variable that this channel references
```

## Example

Example python code included in this directory writes and reads a simple `composable image set` in HDF5 format.

1. run `./test` to create example file(s)
    - `composable.cis` contains several images with several layers that can be composed together, and recolored by several variables.  
2. run `h5dump composable.cis` to inspect the contents of the results. `h5dump` is a tool supported by the HDF5 project - you have to download and install those yourself.

Requirements:

1. `h5py` module
2. HDF5-supported tools (optional)
