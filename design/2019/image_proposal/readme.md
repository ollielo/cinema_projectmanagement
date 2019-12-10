# Composable Channel Image format specification


|  |  |
|--|--|
| Date    | 10 Dec 2019 |
| Version | 1.0 |
| Type    | composablechannelimage |
| Extension | `.cci` |

This specification covers data needed to write out Cinema's `float images` and `composable float images` in the same format.

## Overview

A `composable channel image` is a collection of one or more sets of float values that encode information that can be reconstructed into images. The options for compositing and recoloring depend upon the contents of the `composable channel image`.

The `composable channel image` consists of: 

1. A single two dimensional shape (`MxN`)
1. One or more `layers`, composed of `channels`.

A `channel` is a set of `MxN` values. The values can either be floats or booleans. 

A `layer` is:

1. Of dimension `MxN`.
1. One or more float channels. 
1. An optional `shadow` float channel
1. An optional `depth` float channel 
1. An optional `mask` boolean layer 

Each `float value` may be:

1. A valid float. This includes NaN (point to IEEE spec)
1. Null. This means that there is no data for this value, and it should be considered 'blank', or not present. 

## Storage

A `composable channel image` may be stored in any of several formats.

## Cinema storage

(details of current cinema storage)

## HDF5 storage

The `composable channel image` can be stored in HDF5 format. If it is stored in HDF5 format, it shall have the following structure:

```
/
    dims    (attribute)
    type    (attribute)
    version (attribute)
    layer/ (group)
        <name>/ (one or more named groups)
            depth/  (optional dataset)
            shadow/ (optional dataset)
            mask/   (optional dataset)
            <name>/ (one or more named datasets) 
                globalrange (optional attribute)
```

## Example

Example python code included in this directory writes and reads a simple `composable channel image` in HDF5 format.

1. run `./write` to create several example files:
    - `float.cci` contains a single float image with several variable channels and a single mask.
    - `composable.cci` contains several layers that can be composed together, and recolored by several variables.  
1. run `./dump <filename>` to dump the example files


Requirements:

1. `h5py` module
