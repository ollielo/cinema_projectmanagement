# Composable Image Set format specification

This is a Cinema database that provides parameters for manipuliting a Cinema Composable Image Set (`.cis`) file. This shows definitions for a single image with three layers, each of which has three channels. 

We note that `lighting`, `depth` and `mask` channels may or may not be present in the `output.cis` file, and **consumers** are expected to examine the contents of the file for that information.


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

#### Possible HDF5 Encoding (include depth and lighting channels)
```
/
    parameterlist/
        time   [type:float]
        phi    [type:float]
        theta  [type:float]
        isoval [type:float]
        isovar [type:string]
    parameter/
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
