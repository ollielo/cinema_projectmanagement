# Cinema Database: Composable Image Set parameter specification 

This is a Cinema database that provides parameters for manipulating a Composable Image Set (`.cis`) file. This shows definitions for a single image with three layers, each of which has three channels. 

This proposal exposes `cis:image`, `cis:layer`, and `cis:channel` as parameters. Though we could encode these within a single path parameter, the **consumer** would have to parse the path in order to determine what components are available in the Cinema Database. This proposal requires that the **producer** and **consumer** know about a set of parameter names, but the parsing is not necessary. In addition, the **consumer** knows about the structure of a `cis` image, and how such an image can be manipulated using the data in the table.

## Design 

- The **consumer** must know about the structure of the `.cis` file in order to display it. Therefore, multiple representations are possible in the Cinema database. Two reasonable options are shown below.
- `lighting`, `depth` and `mask` channels shall not be explicitly represented in the Cinema database. In general, they need not be present in the `cis` file, so **consumers** are expected to examine the contents of the file for that information. 

## Example

The following example shows two options for encoding images over:

- **2** timesteps
- **one** camera position
- **2** two isosurface variables:
    - **density**, with **2** values
    - **volfrac**, with **1** value
- **3** variable channel options per isosurface

## Option 1: include images, layers and channels

| time | phi  | theta | isovar  | isoval | cis:image | cis:layer | cis:channel | FILE |
| ---- | ---- | ----- | ------  | ------ | --------- | --------- | ----------- | ---- |
| 1.0  | 10.0 | 10.0  | density | 10.0   | 0000      | 0000      | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | density | 10.0   | 0000      | 0000      | pressure    | output.cis |
| 1.0  | 10.0 | 10.0  | density | 10.0   | 0000      | 0000      | procID      | output.cis |
| 1.0  | 10.0 | 10.0  | density | 20.0   | 0000      | 0001      | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | density | 20.0   | 0000      | 0001      | pressure    | output.cis |
| 1.0  | 10.0 | 10.0  | density | 20.0   | 0000      | 0001      | procID      | output.cis |
| 1.0  | 10.0 | 10.0  | volfrac |  0.9   | 0000      | 0002      | temperature | output.cis |
| 1.0  | 10.0 | 10.0  | volfrac |  0.9   | 0000      | 0002      | pressure    | output.cis |
| 1.0  | 10.0 | 10.0  | volfrac |  0.9   | 0000      | 0002      | procID      | output.cis |
| 2.0  | 10.0 | 10.0  | density | 10.0   | 0001      | 0000      | temperature | output.cis |
| 2.0  | 10.0 | 10.0  | density | 10.0   | 0001      | 0000      | pressure    | output.cis |
| 2.0  | 10.0 | 10.0  | density | 10.0   | 0001      | 0000      | procID      | output.cis |
| 2.0  | 10.0 | 10.0  | density | 20.0   | 0001      | 0001      | temperature | output.cis |
| 2.0  | 10.0 | 10.0  | density | 20.0   | 0001      | 0001      | pressure    | output.cis |
| 2.0  | 10.0 | 10.0  | density | 20.0   | 0001      | 0001      | procID      | output.cis |
| 2.0  | 10.0 | 10.0  | volfrac |  0.9   | 0001      | 0002      | temperature | output.cis |
| 2.0  | 10.0 | 10.0  | volfrac |  0.9   | 0001      | 0002      | pressure    | output.cis |
| 2.0  | 10.0 | 10.0  | volfrac |  0.9   | 0001      | 0002      | procID      | output.cis |

## Option 2: images, channels and layers derived through cis file 

| time | FILE | 
| ---- | ---- | 
| 1.0  | output.cis |
| 2.0  | output.cis |

#### HDF5 Encoding (include depth and lighting channels)
```
/
    variablelist/
        density/
            type float
            min  0.0
            max  1000.0
        temperature/
            type float
            min  0.0
            max  1000.0
        procID/
            type int
            min  0
            max  1024 
    parameterlist/
        time   [type:float]
        phi    [type:float]
        theta  [type:float]
        isovar [type:string]
        isoval [type:float]
    image/
        0000/
            parameter/
                phi   10.0
                theta 10.0
                time   1.0
            layer/
                0000/
                    parameter/     	
                        isovar density
                        isoval 10.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0001/
                    parameter/     	
                        isovar density
                        isoval 20.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0002/
                    parameter/     	
                        isovar volfrac
                        isoval 0.9
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
        0001/
            parameter/
                phi   10.0
                theta 10.0
                time   2.0
            layer/
                0000/
                    parameter/     	
                        isovar density
                        isoval 10.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0001/
                    parameter/     	
                        isovar density
                        isoval 20.0
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
                0002/
                    parameter/     	
                        isovar volfrac
                        isoval 0.9
                    channel/
                        depth
                        lighting
                        temperature
                        pressure
                        procID
```
