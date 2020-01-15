# Cinema Database: Composable Image Set parameter specification 

This is a Cinema database that provides parameters for manipulating a Composable Image Set (`.cis`) file. This shows definitions for a single image with three layers, each of which has three channels. 

This proposal exposes `cis:image`, `cis:layer`, and `cis:channel` as parameters. Though we could encode these within a single path parameter, the **consumer** would have to parse the path in order to determine what components are available in the Cinema Database. This proposal requires that the **producer** and **consumer** know about a set of parameter names, but the parsing is not necessary. In addition, the **consumer** knows about the structure of a `cis` image, and how such an image can be manipulated using the data in the table.

## Design 

- The **consumer** must know about the structure of the `.cis` file in order to display it. Therefore, multiple representations are possible in the Cinema database. Two reasonable options are shown below.
- `lighting`, `depth` and `mask` channels shall not be explicitly represented in the Cinema database. In general, they need not be present in the `cis` file, so **consumers** are expected to examine the contents of the file for that information. 

## Examples

We expect to encode two types of Cinema-specific data in this format. Other encodings are possible, but not supported by this specification.

- [float images](example_float.md)
- [composable images](example_composable.md)

