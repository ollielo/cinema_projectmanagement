# Composable Image Set example

#### Cinema `.csv.` file

| time | phi  | theta | isoval | isovar  | path | FILE |
| ---- | ---- | ----- | ------ | ------  | ---- | -------- |
| 1.0  | 10.0 | 10.0  |  10.0  | density | /image/0000/layers/0000 | output.cis |
| 2.0  | 10.0 | 10.0  |  10.0  | density | /image/0001/layers/0000 | output.cis |

#### Minimal HDF5 Encoding with depth and lighting channels
```
/
  class COMPOSABLE_IMAGE_SET
  dims [1024, 768]
  version 1.0
  flags [CONSTANT_CHANNELS]
  parametertable/
    col_names "time,phi,theta,isoval,isovar,path"
    num_cols 6
    num_rows 2
    columns/
        time
        phi
        theta
        isoval
        isovar
        path
  variables/
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
  image/
    0000/
      layers/
        0000/
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
      layers/
        0000/
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
