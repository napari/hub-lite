
[![License BSD-3](https://img.shields.io/pypi/l/fish-scan.svg?color=green)](https://github.com/ariannaravera/fish-scan/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fish-scan.svg?color=green)](https://pypi.org/project/fish-scan)
[![Python Version](https://img.shields.io/pypi/pyversions/fish-scan.svg?color=green)](https://python.org)
[![tests](https://github.com/ariannaravera/fish-scan/workflows/tests/badge.svg)](https://github.com/ariannaravera/fish-scan/actions)
[![codecov](https://codecov.io/gh/ariannaravera/fish-scan/branch/main/graph/badge.svg)](https://codecov.io/gh/ariannaravera/fish-scan)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/fish-scan)](https://napari-hub.org/plugins/fish-scan)

Plugin to enhance fish detection and analysis for underwater research

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `fish-scan` via [pip]:

    pip install fish-scan



To install latest development version :

    pip install git+https://github.com/ariannaravera/fish-scan.git


## Tutorial

### 1. Color correction

With this tool you can correct colors in your image.

1.	Open your image in napari by grabbing and dropping it or opening from the menu
2.	Click on “Select the area” to select a rectagular area of the color you wanna correct
3.	Draw the rectangle in the area in which you have that color, eg. white area, as in the example below
4.	Select the color name in the dropdown box, eg. in this case white
5.	Click on “Correct color”
6.	If you’re satisfied of the correction made, it is IMPORTANT to select as input “Image”(first box) the name of the new generated image (usually, “Currect_corrected_...)*
7.	Cuntinue your colors corrections re-starting from step 2

#### Nomenclature:
- you MUSH have your original image with its original name (in this case “Group2_FishID_25April…”)
- then, once you start correcting the image, the new generated images will be called as “Current_corrected_*original-name*”
- if you perform the correction more times, your previous corrected image will be named “Previous_corrected_*original-name*” and the new generated always “Current_corrected_*original-name*”.

This allows you to keep as “previous” the result that you already liked and approved, while the “current” you can play and experiment new corrections. 
Be aware that if you select as input image of the correction “previous” this means that you didn’t like the “current” one and it will be overwrite (while the “previous” remain the same), otherwise if you liked the “current” and you use it as input image of the new correction, then the “current” will become “previous” and the new result “current”.
At anytime if you want you can re-start from the original image by selecting it as input image (original image is NEVER changed).
 
### 2. Set Scale
With this tool you can automatically measure your fish if a scale is in the image.

1.	Click on “Select 1 cm” and draw a line on the scale represeting 1cm, as in this example:
 
2.	Click on “Set scale” and your fish will be automaticall measure in your final analysis with this scale
 
### 3. Segmentation & Analysis
With this tool you can segment your fish.

Steps:
1.	Select the “Image” you want to analyse (be aware of the nomenclature*)
2.	Click “Select fish area” button
3.	Start drawing your mask with the brush (yellow arrow below). I suggest to start drwaing the fish contours and then with the paint bucket (red arrow below) fill the inside. Adjust it with the eraser (orange arrow below) if needed
    
4.	Select the output folder you want the results saved in by clicking “Browse”
5.	Finally, click on “Analyse the fish” to generate your analysis

Here is an example of the results you obtain from it:
•	two graphs per image,
o	one representing the percentage of the 3 dominant color you want to study (black, white and orange) 
 
o	one with the composition of the real RGB values found in the image (the ones that are categorized in the 3 main classes you have in graph 1)
 

•	one csv file in which there are the number of black, white and orange pixels, their percentages (same values of graph 1), the length of the fish in pixels (always provided) and the length converted in cm (if a scale was provided).
o	If in the output folder chosen there were already a previously created csv we will append to that the new info, otherwise a new csv is created.
 


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"fish-scan" is free and open source software

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

[file an issue]: https://github.com/ariannaravera/fish-scan/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
