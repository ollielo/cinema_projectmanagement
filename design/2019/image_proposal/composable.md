# Composable Image Set format specification

This is a Cinema database that provides parameters for manipulating a Composable Image Set (`.cis`) file. This shows definitions for a single image with three layers, each of which has three channels. 

This proposal exposes `cis:image`, `cis:layer`, and `cis:channel` as parameters. Though we could encode these within a single path parameter, the **consumer** would have to parse the path in order to determine what components are available in the Cinema Database. This proposal requires that the **producer** and **consumer** know about a set of parameter names, but the parsing is not necessary. In addition, the **consumer** knows about the structure of a `cis` image, and how such an image can be manipulated using the data in the table.

We note that `lighting`, `depth` and `mask` channels are not explicitly represented in the Cinema database. In general, they need not be present in the `cis` file, so **consumers** are expected to examine the contents of the file for that information. 

## Option 1: include all layers

| time | phi  | theta | isoval | isovar  | cis:image | cis:layer | cis:channel | resource |
| ---- | ---- | ----- | ------ | ---- | ----- | ----- | ------- | -------- |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | pressure | output.cis |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | procID | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | pressure | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | procID | output.cis |
| 1.0  | 10.0 | 10.0  | 30.0   | density | 0000 | 0002 | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | 30.0   | density | 0000 | 0002 | pressure | output.cis |
| 1.0  | 10.0 | 10.0  | 30.0   | density | 0000 | 0002 | procID | output.cis | 

## Option 2: channels are introspected (not available through the Cinema database)

| time | phi  | theta | isoval | isovar  | cis:image | cis:layer | resource |
| ---- | ---- | ----- | ------ | ---- | ----- | ----- | ------- | -------- |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | output.cis |
| 1.0  | 10.0 | 10.0  | 30.0   | density | 0000 | 0002 | output.cis |

#### HDF5 Encoding (include depth and lighting channels)
```
/
    parameterlist/
        time   [type:float]
        phi    [type:float]
        theta  [type:float]
        isoval [type:float]
        isovar [type:string]
    parameters/
        time 1.0
    images/
        0000/
            parameters/
                phi 10.0
                theta 10.0
            layers/
                0000/
                    parameters/     	
                        isoval 10.0
                        isovar density
                    channels/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0001/
                    parameters/     	
                        isoval 20.0
                        isovar density
                    channels/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0002/
                    parameters/     	
                        isoval 30.0
                        isovar density
                    channels/
                        depth
                        lighting
                        temperature
                        pressure
                        procID

```
