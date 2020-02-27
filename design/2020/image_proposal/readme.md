# Composable Image Set format specification

This repository includes specification, documenation and examples for the Cinema **composable image set** data type.

|    |    |
|----|----|
| Date    | 10 Dec 2019 |
| Version | 1.0 |
| Type    | COMPOSABLE_IMAGE_SET |
| Extension | `.cis` |
| Authors | David H. Rogers, John Patchet, Ethan Stam, Dave DeMarle, Sebastian Jourdain, Jonas Lucasczyk |

## Current specification

- [v1.0](spec/cis_specification_v1-0.md)

## Overview

Cinema creates image-based data that is useful within Cinema but also to a wider set of applications. The format is discussed in <sup>[1]</sup>. The purpose of this specification is to:

1. Completely describe this data type, 
2. Standardize its storage, and 
3. Enable its use by any **producer** or **consumer**. 

## Use cases

Here are the current use cases:

- [Basic use case](spec/usecases/01/use-case-01.md)
- [ECP 2020 workflow](spec/usecases/02/use-case-02.md)

## Cinema Database Reference Example

The `.cis` format is a way of encoding specific types of information. It is up to a **producer** and **consumer** of the data to determine the semantic meaning of the encoded data.

Providing semantic meaning in a Cinema database entails providing metadata about the image/layer/channel components, and referencing a path in the `.cis` file. This is exactly analogous to providing a path to disk, except that the `FILE` that the path maps to is a `.cis` file. 

[This proposal](spec/examples/example_composable.md) shows how this data should be encoded in a Cinema database.


## Open areas 

One question is how to represent to a consumer enough of a state so that the image can be reconstructed to an expected result. The specification and storage models should include the following information, so that the producer and consumer can perform an apples-to-apples comparison of the images:

1. Default State. This should include current image, layer states (on or off), global variable ranges and default color maps.
2. Color maps


## References

1. James Ahrens, Sebastien Jourdain, Patrick O'Leary, John Patchett, David H. Rogers, and Mark Petersen. An image-based approach to extreme scale in situ visualization and analysis. In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '14). IEEE Press, Piscataway, NJ, USA, 424-434, 2014.
