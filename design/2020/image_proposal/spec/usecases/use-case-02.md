# ECP end-to-end use case

The goal of this use case is to develop and test components and capabilities that bring ECP ALPINE pipelines up to date with current Cinema specifications and data types.

We note that we must define timesteps, isocontour values and variable values to complete this use case.

1. Warp3D is run coupled with ASCENT to produce a Cinema database of a visualization of selected isosurface values, with appropriate visualization context (colorbars, scales, etc.). The isosurface values shall be a subset of those defined by G. Weber's topological selection algorithm. Those values shall be defined outside of this workflow.
1. A Cinema database is produced over multiple timesteps to produce a `.cis` dataset that includes:
    - three timesteps, valued at (t1, t2, t3)
    - phi/theta camera rotations over the following values:
        - phi (0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0)
        - theta (0.0, 15.0, 30.0, 45.0)
    - Three (3) isosurface values, each colored by two (2) variables.
        - isosurface values: (iso1, iso2, iso3) 
        - variable values: (v1, v2)
1. The entire resulting dataset shall be included in a single `.cis` file. For this file:
    - each `[timestep, phi, theta]` combination shall be a separate `.cis` image.
    - within each image, the visualization context (colorbars, scales, etc.) shall be a layer
    - within each image, each isosurface shall be a layer.
        - within each of these layers, each variable value shall be a channel.
1. A python notebook viewer is run to visualize the resulting `.cis` data. The viewer shall read and parse the `.cis` file and provide appropriate sliders, on/off buttons, and selection controls to: 
    - Control time and viewing angle
    - Turn image layers on and off
    - Select and color channels for layers
