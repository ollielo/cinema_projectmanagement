# Composable Image Set format specification


|  |  |
|--|--|
| Date    | 10 Dec 2019 |
| Version | 1.0 |
| Type    | composableimageset |
| Extension | `.cis` |

Cinema creates two types of data that are useful both within Cinema, but also to a wider set of applications. The formats are discussed in [1]. In order to standardize these data types and enable their use in other applications, we propose this standard specification.

This specification covers data needed to write out Cinema's `float images` and `composable float images` in the same format.

1. `float images` contain float values for a single image. These are used to compute information about a variable from a rendered object, or to allow an image to be recolored with different color maps after it has been rendered. 
1. `composable images` contain several layers that can be composited to show a correct rendering from a specific camera position. These can also be recolored with different color maps. Using a set of these images, one can turn on and off different parts of a rendering, making the resulting image more interactive.

Often these images are useful to collect in sets, so this specification defines a format for a collection of such images.

## Overview

A `composable image set` is a collection of one or more images, each of which are sets of float values that encode information that can be reconstructed into images. The options for compositing and recoloring depend upon the contents of the `composable image set`.

The `composable image set` consists of: 

1. A single two dimensional shape (`MxN`)
1. One or more `images`, composed of `layers`. `Layers` are composed of `channels`.

A `layer` is:

1. Of dimension `MxN`.
1. One or more float channels. 
1. An optional `shadow` float channel
1. An optional `depth` or an optional `mask` channel. It cannot contain both a `depth` and a `mask` layer. 
    1. `depth` is a float channel
    1. `mask` is a boolean channel 

A `channel` is a set of `MxN` values. The values can either be `float values` or booleans. 

Each `float value` may be:

1. A valid float. This includes NaN (point to IEEE spec)
1. Null. This means that there is no data for this value, and it should be considered 'blank', or not present. 

## Storage

A `composable image set` may be stored in any of several formats.

## Cinema storage

(details of current cinema storage)

## HDF5 storage

The `composable image set` can be stored in HDF5 format. If it is stored in HDF5 format, it shall have the following structure:

```
/
    dims    (attribute) (required)
    type    (attribute) (required)
    version (attribute) (required)
    images/ (group) (required)
        <name>/ (one or more named groups required)
            layer/ (group) (required)
                <name>/ (one or more named groups required)
                    depth/  (optional dataset)
                    shadow/ (optional dataset)
                    mask/   (optional dataset)
                    <name>/ (one or more named datasets required) 
                        globalrange (optional attribute)
```

## Example

Example python code included in this directory writes and reads a simple `composable image set` in HDF5 format.

1. run `./write` to create several example files:
    - `float.cci` contains a single image with several variable channels and a single mask.
    - `composable.cci` contains several images with several layers that can be composed together, and recolored by several variables.  
1. run `./dump <filename>` to dump the example files


Requirements:

1. `h5py` module

## References

1. James Ahrens, SÃƒÂ©bastien Jourdain, Patrick O'Leary, John Patchett, David H. Rogers, and Mark Petersen. An image-based approach to extreme scale in situ visualization and analysis. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '14). IEEE Press, Piscataway, NJ, USA, 424-434, 2014.
