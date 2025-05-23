
[![License BSD-3](https://img.shields.io/pypi/l/napari-zplane-depth-colorizer.svg?color=green)](https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-zplane-depth-colorizer.svg?color=green)](https://pypi.org/project/napari-zplane-depth-colorizer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-zplane-depth-colorizer.svg?color=green)](https://python.org)
[![tests](https://github.com/maihanhoang/napari-zplane-depth-colorizer/workflows/tests/badge.svg)](https://github.com/maihanhoang/napari-zplane-depth-colorizer/actions)
[![codecov](https://codecov.io/gh/maihanhoang/napari-zplane-depth-colorizer/branch/main/graph/badge.svg)](https://codecov.io/gh/maihanhoang/napari-zplane-depth-colorizer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-zplane-depth-colorizer)](https://napari-hub.org/plugins/napari-zplane-depth-colorizer)

A simple plugin for 3d+t files that visualizes z-planes in 3 colors for depth information. 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

This plugin can colorize and provide depth information on single-channel 3D+t files. The color coding enhances the visibility of structures and the detection/annotations of dynamic events. 

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/plugin_demo.gif" width="100%" />
</p>

Identifying dynamic events such as cellular divisions can be challenging in 3D time-lapses of developing tissues such as organoids or embryos. Visualizing and annotating such events in dense 3D stacks obtained by light-sheet or two-photon microscopy where nuclei are almost in contact is especially challenging. With this visualization method, the tissue section can be "augmented" in 3D by visualizing the surrounding tissue layers in different colors. 

This plugin is for bioimaging researchers who need to annotate events in time lapses of dense tissues. It supports 3D+t stacks in the TZYX format. 

## Installation

You can install `napari-zplane-depth-colorizer` via [pip]:

    pip install napari-zplane-depth-colorizer

To install latest development version :

    pip install git+https://github.com/maihanhoang/napari-zplane-depth-colorizer.git

## Quick Start
A sample file can be found at `src/napari_zplane_depth_colorizer/data/3D+t.tif`

1. Open a 3D+t tif in napari, make sure it is in TZYX format
2. If it's a 4D file, it will automatically appear in the drop-down menu of *Input*
3. Use default parameters for *Z-Projection Type* and *Depth Range*
4. Click *Merge to RGB*
5. Result will appear in the viewer and in *Output*
6. To save, select the colored stack in *Output*, select saving format (*Save as*), and click *Save RGB*

## Parameters
There are two depth augmentation parameters for each RGB color channel: Z-Projection Type and Depth Range. Depth Range indicates which and how many z-planes are projected for a channel. The Z-Projection Type specifies which type of projection is applied. The **How it works** section below might help you understand the parameters better.

### Z-Projection Types 
The Z-projection types are the same ones found in [Fiji](https://imagej.net/software/fiji/), except for "Raw. "Raw is the original stack without any projection.

### Depth Range
- Depth Range is a range and consists of two numbers [range_start, range_end]. The range is inclusive and requires range_start <= range_end. 

- Exception if Z-Projection Type is "Raw" since no z-projection is applied. The Depth Range for Raw can either be empty (equals 0 then) or a single number. 

- The Depth Range indicates the z-planes relative to the reference plane that are projected and then assigned to a color channel. The reference plane is the plane for which the color merging is currently computed.

- In the illustration below, the current reference plane is the 4. plane (indicated by the color wheel in the right stack). A Depth Range of [-3, -1] for the red channel denotes the first three planes above the reference plane. Similarly, a Depth Range of [1, 2] for the blue channel indicates the first two planes below the reference plane. Negative numbers are for the planes above, and positive numbers are for ones below the reference plane. 0 is the same as the reference plane (the green plane in the illustration).   

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/entire_stack_zproj.jpg" width="100%" />
</p>


## How it works
### Creating a colored image from a single-channel stack

To colorize a single-channel stack, multiple z-planes are assigned to different color (RGB) channels and then overlaid to create a composite colored image. For a simple z-stack with three planes, the 1. plane is assigned to red, the 2. to green, and the 3. plane to blue. They are overlaid/merged to create a single composite RGB-color plane. In the composite image, multiple z-planes are displayed simultaneously, with the colors providing the depth information. In this example, red indicates that cells are in the upper, while blue cells are in the deeper z-planes. The colors make it easier to detect and track cells that move or split in the z-direction.  


<!---------
In other words, instead of having multiple channels from different fluorescence labels, the z-planes are treated as different channels and then merged to create a composite image.


<img src="./assets/3_plane_stack.gif" alt="Demo GIF" style="width:100%;">
-------->
<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/3_plane_stack.gif" width="100%" />
</p>

On the left is an image of a single plane of an organoid and on the right is the colorized plane. To create the colors, the same plane was overlaid with the direct upper and lower plane, as shown in the illustration above. 
<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/img_gray.png" width="49%" />
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/img_color.png" width="49%" /> 
</p>

### Colorizing the entire stack
To obtain a colorized stack of the same size as the original stack, the merging is applied for each z-plane. At the boundaries, the colors can differ, as there are no further z-planes to assign to a color channel. For example, the first plane in the colorized stack consists of an overlay of only two planes in green and blue, which results in a blue/green/cyan-colored image. Similarly, the last plane of the colorized stack is a red/green/yellowish image since it lacks a blue channel.    

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/entire_stack.gif" width="100%" />
</p>

### Varying the depth with z-projections
It is also possible to vary the depth and overlay more than three planes. To do this, a z-projection is applied to the planes before assigning them to a color and merging. In the illustration below, a different number of planes is assigned to each color. Before merging the three RGB color channels, a z-projection is applied if more than one plane is assigned to a color. In the illustration below, three planes are selected for the red color channel. A z-projection (e.g. average intensity) is applied to generate a single plane for the red channel. This z-projected plane is merged with the raw, green plane and the z-projected plane of the blue channel. 


<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/entire_stack_zproj.jpg" width="100%" />
</p>

For the entire stack:
<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/entire_stack_zproj.gif" width="100%" />
</p>

On the left is an image of a single plane of an organoid, and on the right is the colorized plane. To create the colors, the same plane was overlaid with three upper and two lower z-planes, as shown in the illustration above. 

<p align="middle">
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/img_gray.png" width="49%" />
  <img src="https://github.com/maihanhoang/napari-zplane-depth-colorizer/raw/main/assets/img_color_zproj.png" width="49%" /> 
</p>

## Acknowledgements
[Sham Tlili](https://scholar.google.com/citations?user=8ykCpTIAAAAJ&hl=fr) provided the sample data and developed the visualization method implemented in this plugin

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-zplane-depth-colorizer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/maihanhoang/napari-zplane-depth-colorizer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
