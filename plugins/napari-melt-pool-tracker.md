<img style="float: right;" src="https://imaging.epfl.ch/resources/logo-for-gitlab.svg">


# napari-melt-pool-tracker
Developed by the [EPFL Center for Imaging](https://imaging.epfl.ch/) for the [Thermomechanical Metallurgy Laboratory](https://www.epfl.ch/labs/lmtm/) in Sep 2023.
Plugin for tracking the width and depth of the melt pool and keyhole in x-ray images of laser powder bed fusion experiments.

[![License BSD-3](https://img.shields.io/pypi/l/napari-melt-pool-tracker.svg?color=green)](https://github.com/EPFL-Center-for-Imaging/napari-melt-pool-tracker/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-melt-pool-tracker.svg?color=green)](https://pypi.org/project/napari-melt-pool-tracker)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-melt-pool-tracker.svg?color=green)](https://python.org)
[![tests](https://github.com/EPFL-Center-for-Imaging/napari-melt-pool-tracker/workflows/tests/badge.svg)](https://github.com/EPFL-Center-for-Imaging/napari-melt-pool-tracker/actions)
[![codecov](https://codecov.io/gh/EPFL-Center-for-Imaging/napari-melt-pool-tracker/branch/main/graph/badge.svg)](https://codecov.io/gh/EPFL-Center-for-Imaging/napari-melt-pool-tracker)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-melt-pool-tracker)](https://napari-hub.org/plugins/napari-melt-pool-tracker)
[![DOI](https://zenodo.org/badge/700413345.svg)](https://zenodo.org/doi/10.5281/zenodo.11366048)


----------------------------------

## Installation

You can install `napari-melt-pool-tracker` via [pip]:

    pip install napari-melt-pool-tracker

# Getting Started with napari-melt-pool-tracker

## Reading Data

- The `napari-melt-pool-tracker` plugin can read h5 files from the ID19 and TOMCAT beam lines.
- When opening an h5 file in napari, select the "Melt Pool Tracker" as the reader for the mentioned beamlines.
- Once the data is loaded, you have the option to save the layer as a tif file if needed.

## Pre-processing

- For large images, it is recommended to crop them in both time and space to include only the relevant parts of the image stack.

## 1. Determine Laser Speed and Position

- This step helps identify the laser in the images for later reslicing the stack with a moving window following the laser.
- It generates a projection of the stack along the y-axis, creating an x-t image where the laser's position appears as an oblique line in the projection.

**To perform this step:**

1. Select the stack you want to work on using the "Input" drop-down menu.
2. Choose one of three projection modes:
   - Default: Maximum projection along y.
   - Pre mean: Divide each frame by the mean projection along the t-axis (to remove background) and then perform a maximum projection along y.
   - Post median: Perform a maximum projection along y and then divide the projected images by a median-filtered version in the x-direction (to remove horizontal strips).
3. Click "Run" to generate a new layer with the projected image and a shapes layer with a line.
4. Select the line layer, use the "Select vertices" tool to match the line with the laser in the projected image.

## 2. Reslice with Moving Window

- This step reslices the stack with a moving window that follows the laser's position.

**To perform this step:**

1. Select the input stack using the "Stack" drop-down menu.
2. Choose the line layer with the laser's position using the "Line" drop-down menu.
3. Adjust the "Left margin" and "Right margin" sliders to set the size of the window to the left and right of the laser's position.
4. Click "Run" to create three new layers: a resliced stack, a shapes layer indicating the laser's position based on your previous annotation, and a shapes layer with lines indicating the window's position in the original image.
5. If the window size doesn't fit the melt pool correctly, adjust it using the margin sliders. Disable the "Auto run" checkbox for large stacks to control when reslicing occurs.

## 3. Filter Image

- This step aims to reduce noise in the images by applying a median filter.

**To filter the image:**

- Select the resliced layer as the input.
- Use the "Kernel" sliders to set the size of the median filter along different axes.
- Disable "Auto run" for large stacks due to the computational cost. After median filtering, the function applies Otsu thresholding to remove the background. Adjust the contrast as needed.

## 4. Calculate Radial Gradient

- This step calculates the gray value gradient in the radial direction with respect to a point on the surface, forming the origin. You can set the horizontal position of the origin using the position slider.

**To calculate the radial gradient:**

- Select the resliced and filtered stack as input.
- Adjust the contrast for the new radial gradient layer.

## 5. Annotate

- Annotation of points is done using the [napari-cursor-tracker](https://www.napari-hub.org/plugins/napari-cursor-tracker) plugin.

**To annotate points:**

- Select any of the resliced layers as your reference image.
- Change the name in the "Name of the tracked point" text box to define the point you want to track, e.g., 'MP depth'.
- Click "Add new layer" to create a new points layer with the specified name, automatically selected as the active layer.
- Start tracking by pressing 't' on your keyboard. Enable "Auto play when tracking is started" for automatic playback.
- Adjust playback parameters as needed. Setting "Loop mode" to 'once' is advised to prevent overwriting tracked points. You can track points manually by scrolling through slices/frames (hold down `ctrl`) and saving your cursor positions at each index change.

## Saving and Processing Results

- You can save the 'window_coordinates' layer and point layers with tracked points as CSV files for further processing with external software.


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-melt-pool-tracker" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
