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
                        pressure
                        procID
                0001/
                    parameter/     	
                        cut 1
                    channel/
                        depth
                        lighting
                        temperature

```
