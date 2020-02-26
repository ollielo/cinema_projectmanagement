# ECP end-to-end use case

1. Warp3D is run coupled with ASCENT to produce a Cinema database of a visualization of selected isosurface values. 
2. A Cinema database is produced over multiple timesteps to produce a `.cis` dataset that includes:
    - three timesteps, valued at (t1, t2, t3)
    - phi/theta camera rotations over the following values:
        - phi (0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0)
        - theta (0.0, 15.0, 30.0, 45.0)
    - Three (3) isosurface values, each colored by two (2) variables.
        - isosurface values: (iso1, iso2, iso3) 
        - variable values: (v1, v2)
3. A python notebook viewer is run to visualize the resulting `.cis` data. The viewer shall read and parse the `.cis` file and provide appropriate sliders, on/off buttons, and selection controls to: 
    - Control time and viewing angle
    - Turn image layers on and off
    - Select and color channels for layers
