# A Simple Use Case

This use case describes a workflow on a specific `.cis` file.

A **producer** saves a `.cis` file with:
- a `variable` named `temperature`
- a `colormap` named `rainbow`
- an `image` named `0000` with:
    - `layer` named `f00`
        - `variable` defined as `temperature`
        - `colormap` defined as `rainbow`
- an `image` named `0001` with:
    - `layer` named `f00`
        - `variable` defined as `temperature`
        - `colormap` defined as `rainbow`

A **consumer** reads the file and displays a single, initial image.

In the absence of other information, the application will initialize a single `image`, `layer` and `channel`. The `image`, `layer` and `channel` chosen are the first alphabetically for each set.
