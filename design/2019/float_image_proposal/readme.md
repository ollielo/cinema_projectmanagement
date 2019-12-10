# Float image format specification

Date: 10 Dec 2019

Version: 1.0

## Overview

A `float channel image` is a collection of one or more `MxN` sets of values. 

The `float channel image` has: 

1. A two dimensional shape (`MxN`)
1. A version number, referencing the version of this specification
1. A type designation, which is the type designation included in this specification
1. One or more sets of `values` of dimension `MxN`.

Each set of `values` shall have the following meta data:

1. A name. Each name shall be unique within the scope of this `float channel image`.
1. Global range (min, max). This is the global context for the range of the value.

Each `value` may be:

1. A valid float. This includes NaN (point to IEEE spec)
1. Null. This means that there is no data for this value, and it should be considered 'blank', or not present. 

## Storage

A `float channel image` may be stored in any of several formats.

## Cinema storage

(details of current cinema storage)

## HDF5 storage

The `float channel image` can be stored in HDF5 format. If it is stored in HDF5 format, it shall have the following structure:

```
    attr: width
    attr: height
    attr: type
    attr: version
    group: channels
        dataset: <named>
            attr: globalrange (optional)
```

## Example

Example python code included in this directory writes and reads a simple `float channel image` in HDF5 format.

Requirements:

1. `h5py` module
