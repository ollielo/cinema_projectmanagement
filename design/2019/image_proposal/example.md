# Composable Image Set example

#### Cinema `.csv.` file

| time | phi  | theta | isoval | isovar | cut | path | resource |
| ---- | ---- | ----- | ------ | ------ | --- | ---- | -------- |
| 1.0  | 10.0 | 10.0  | 10.0   | density | | /image/0000/layers/0000 | output.cis |
| 1.0  | 10.0 | 10.0  |        |         |1| /image/0000/layers/0001 | output.cis |


#### HDF5 Encoding with depth and lighting channels
```
/
    parameterlist/
        isoval [type:float]
        isovar [type:string]
        cut    [type:int]
        var    [type:string]
    image/
        0000/
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
                        cut 1
                    channels/
                        depth
                        lighting
                        temperature

```
