# Float image format specification

Date: 10 Dec 2019

Version: 1.0

## Overview

A float image is a set of one or more `MxN` set of values. 

The set of values has:

1. A shape (`MxN`)
2. A version number, referencing the version of this specification
3. A type designation, which is the type designation included in this specification
4. A set of `MxN` `values`

Each set of `values` shall have the following meta data:

1. A name. Each name shall be used only once per float image.
1. Global range (min, max). This is the global context for the range of the value.

Each `value` may be:

1. A valid float. This includes NaN (point to IEEE spec)
2. Null. This means that there is no data for this value, and it should be considered 'blank', or not present. 

## Storage

A float image may be stored in any of several formats.

## Cinema storage

(details of current cinema storage)

## HDF5 storage

The float image can be stored in HDF5 format. If it is stored in HDF5 format, it shall have the following structure:

```
    attr: width
    attr: height
    attr: type
    attr: version
    group: channels
        dataset: mask
        dataset: <named>
            attr: globalrange
```

## Example

Example python code included in this directory writes and reads a simple float image in HDF5 format.

Requirements:

1. `h5py` module
