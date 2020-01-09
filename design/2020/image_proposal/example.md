# Composable Image Set example

#### Cinema `.csv.` file

| time | phi  | theta | isoval | isovar | cut | path | FILE |
| ---- | ---- | ----- | ------ | ------ | --- | ---- | -------- |
| 1.0  | 10.0 | 10.0  | 10.0   | density | | /image/0000/layers/0000 | output.cis |
| 1.0  | 10.0 | 10.0  |        |         |1| /image/0000/layers/0001 | output.cis |


#### HDF5 Encoding with depth and lighting channels
```
/
    class COMPOSABLE_IMAGE_SET
    dims [1024, 768]
    version 1.0
    flags [CONSTANT_CHANNELS]
    variablelist/
        temperature/
            type float
            min  0.0
            max  1000.0
        pressure/
            type float
            min  0.0
            max  5000.0
        procID/
            type int
            min  0
            max  1024 
    parameterlist/
        time    [type:float]
        phi     [type:float]
        theta   [type:float]
        isoval  [type:float]
        isovar  [type:string]
    image/
        0000/
            layers/
                0000/
                    parameter/     	
                        isoval 10.0
                        isovar density
                    channel/
                        depth
                        lighting
                        temperature
                            variable temperature
                        pressure
                            variable pressure
                        procID
                            variable procID
                0001/
                    parameter/     	
                        cut 1
                    channel/
                        depth
                        lighting
                        temperature
                            variable temperature
                        pressure
                            variable pressure
                        procID
                            variable procID

```
