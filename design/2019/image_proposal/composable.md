# Cinema Database: Composable Image Set parameter specification 

This is a Cinema database that provides parameters for manipulating a Composable Image Set (`.cis`) file. This shows definitions for a single image with three layers, each of which has three channels. 

This proposal exposes `cis:image`, `cis:layer`, and `cis:channel` as parameters. Though we could encode these within a single path parameter, the **consumer** would have to parse the path in order to determine what components are available in the Cinema Database. This proposal requires that the **producer** and **consumer** know about a set of parameter names, but the parsing is not necessary. In addition, the **consumer** knows about the structure of a `cis` image, and how such an image can be manipulated using the data in the table.

## Design 

- The **consumer** must know about the structure of the `.cis` file in order to display it. Therefore, multiple representations are possible in the Cinema database. Two reasonable options are shown below.
- `lighting`, `depth` and `mask` channels shall not be explicitly represented in the Cinema database. In general, they need not be present in the `cis` file, so **consumers** are expected to examine the contents of the file for that information. 

## Option 1: include images, layers and channels

| time | phi  | theta | isoval | isovar  | cis:image | cis:layer | cis:channel | FILE |
| ---- | ---- | ----- | ------ | ---- | ----- | ----- | ------- | -------- |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | pressure | output.cis |
| 1.0  | 10.0 | 10.0  | 10.0   | density | 0000 | 0000 | procID | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | pressure | output.cis |
| 1.0  | 10.0 | 10.0  | 20.0   | density | 0000 | 0001 | procID | output.cis |
| 2.0  | 10.0 | 10.0  | 10.0   | density | 0001 | 0000 | temperature | output.cis |
| 2.0  | 10.0 | 10.0  | 10.0   | density | 0001 | 0000 | pressure | output.cis |
| 2.0  | 10.0 | 10.0  | 10.0   | density | 0001 | 0000 | procID | output.cis |
| 2.0  | 10.0 | 10.0  | 20.0   | density | 0001 | 0001 | temperature | output.cis |
| 2.0  | 10.0 | 10.0  | 20.0   | density | 0001 | 0001 | pressure | output.cis |
| 2.0  | 10.0 | 10.0  | 20.0   | density | 0001 | 0001 | procID | output.cis |

## Option 2: images, channels and layers derived through cis file 

| time | FILE | 
| ---- | ---- | 
| 1.0  | output.cis |

#### HDF5 Encoding (include depth and lighting channels)
```
/
    parameterlist/
        time   [type:float]
        phi    [type:float]
        theta  [type:float]
        isoval [type:float]
        isovar [type:string]
    image/
        0000/
            parameter/
                phi 10.0
                theta 10.0
                time 1.0
            layer/
                0000/
                    parameter/     	
                        isoval 10.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0001/
                    parameter/     	
                        isoval 20.0
                        isovar density
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
        0001/
            parameter/
                phi 10.0
                theta 10.0
                time 2.0
            layer/
                0000/
                    parameter/     	
                        isoval 10.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0001/
                    parameter/     	
                        isoval 20.0
                        isovar density
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID

```
