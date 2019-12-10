# Composable Channel Image format specification


|  |  |
|--|--|
| Date    | 10 Dec 2019 |
| Version | 1.0 |
| Type    | composablechannelimage |
| Extension | `.cci` |


## Overview

A `composable channel image` is a collection of one or more sets of float values that encode information that can be reconstructed into images.

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
    attr: width <int>
    attr: height <int>
    attr: type "composablechannelimage"
    attr: version <string>
    group: "layer"
        group: "ID"
            dataset: "depth" (optional)
                attr: "type" (optional)
            dataset: "shadow" (optional)
            dataset: <name>
                attr: globalrange (optional)
            dataset: <name>
                attr: globalrange (optional)
            ...
```

## Example

Example python code included in this directory writes and reads a simple `composable channel image` in HDF5 format.

Requirements:

1. `h5py` module
