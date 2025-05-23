
[![License BSD-3](https://img.shields.io/pypi/l/MMV-playground.svg?color=green)](https://github.com/MMV-Lab/MMV-playground/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/MMV-playground.svg?color=green)](https://pypi.org/project/MMV-playground)
[![Python Version](https://img.shields.io/pypi/pyversions/MMV-playground.svg?color=green)](https://python.org)
[![tests](https://github.com/MMV-Lab/MMV-playground/workflows/tests/badge.svg)](https://github.com/MMV-Lab/MMV-playground/actions)
[![codecov](https://codecov.io/gh/MMV-Lab/MMV-playground/branch/main/graph/badge.svg)](https://codecov.io/gh/MMV-Lab/MMV-playground)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/MMV-playground)](https://napari-hub.org/plugins/MMV-playground)

This plugin is aimed at researchers in biology and medicine who want to segment and analyze 2D microscopy images. It offers intuitive tools for common pre-processing and analysis tasks.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `MMV-playground` via [pip]:

    pip install MMV-playground

To install latest development version :

    pip install git+https://github.com/MMV-Lab/MMV-playground.git

## Documentation

This plugin for the graphics software Napari is designed to analyze two-dimensional microscopy images. Images should be provided in grayscale format, as colored images are not supported. The plugin includes seven core functions for image analysis:

1. Intensity normalization  
2. Smoothing  
3. Background correction  
4. Spot-shape filter  
5. Filament-shape filter  
6. Thresholding  
7. Topology-preserving thinning  

We provide an [introduction](https://github.com/MMV-Lab/MMV-playground/blob/main/docs/introduction.md) to explain the different functions of this plugin.

### **How to Start and Use the Plugin**

To start the plugin, open Napari, go to the "Plugins" menu, and select "MMV-playground (MMV-playground)." The MMV-playground interface will appear on the right-hand side of the Napari window, displaying seven buttons, each corresponding to one of the available functions. Clicking a button opens a dialog box where you can select an image, adjust the parameters for the chosen function, and execute it by pressing the "Run" button. Clicking the function button again collapses the dialog box.

### Screenshot

Here is a preview of the MMV-playground plugin in action:

![MMV-playground Plugin Screenshot](https://raw.githubusercontent.com/MMV-Lab/MMV-playground/main/docs/images/plugin_screenshot.png)

---

### **Intensity Normalization**

This function adjusts the image intensity to enhance contrast and improve uniformity. Two percentage values are required:  
- *Lower percentage (0–5%)*: Defines the darkest portion of the image to ignore as background noise, which is set to a fixed value.  
- *Upper percentage (95–100%)*: Specifies the brightest portion of the image to be capped, preventing overexposure.  

The plugin calculates the respective percentiles based on these values. Intensities below the lower percentile are clipped, and those above the upper percentile are also capped. Finally, all pixel intensities are rescaled to the range [0, 1].

---

### **Smoothing**

This function reduces noise to enhance image clarity. Two methods are available:  
- *Gaussian smoothing*  
- *Edge-preserving smoothing*: Retains edges (e.g., cell boundaries) while reducing noise.  

---

### **Background Correction**

This function removes uneven illumination or background artifacts using a filter. The key parameter is:  
- *Kernel size (1–100)*: Determines the spatial scale of the background correction. Smaller kernel sizes remove local noise, while larger sizes correct for broader illumination variations.  

The [scipy.ndimage.white_tophat] function is used to perform the correction, making this method effective for images with dark backgrounds.

---

### **Spot-Shape Filter**

This filter detects circular structures, such as cell nuclei or fluorescent spots. It is based on the [scipy.ndimage.gaussian_laplace] function and requires:  
- *Sigma (σ)*: Controls the size of the spots to detect. Smaller sigma values target smaller spots, while larger values focus on larger structures.

---

### **Filament-Shape Filter**

This filter highlights elongated structures like cytoskeletal fibers or blood vessels. Using the [aicssegmentation.core.vessel.vesselness2D] function, the key parameter is:  
- *Sigma (σ)*: Specifies the width of the detected filaments. Lower values detect thinner structures, while higher values identify thicker ones.

---

### **Thresholding**

This function segments the image into binary regions by separating the signal from the background. Users can choose one of four thresholding methods:  
- *Otsu*: Best for images with clear separation between background and signal intensities.  
- *Li*: Suitable for uniformly illuminated images.  
- *Triangle*: Effective for asymmetrical intensity distributions.  
- *Sauvola*: Ideal for images with uneven illumination.  

The result is a binary image where pixels above the threshold are set to 1 (signal), and all others are set to 0 (background).

---

### **Topology-Preserving Thinning**

This function extracts the skeleton of structures while maintaining their connectivity. Two parameters are required:  
- *Minimum thickness (0.5–5)*: Defines the smallest allowable thickness of structures before thinning.  
- *Thin (1–5)*: Controls the degree of thinning, reducing structure width while preserving topology (e.g., network connections).  

This is particularly useful for analyzing vascular or cellular networks.

---

### **What Is Missing?**

Currently, unit tests are not implemented, and internal documentation of the source code is still in progress.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"MMV-playground" is free and open source software

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

[file an issue]: https://github.com/MMV-Lab/MMV-playground/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

[scipy.ndimage.gaussian_filter]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html
[itk.GradientAnisotropicDiffusionImageFilter]: https://itk.org/Doxygen/html/classitk_1_1GradientAnisotropicDiffusionImageFilter.html
[scipy.ndimage.white_tophat]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.white_tophat.html
[scipy.ndimage.gaussian_laplace]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_laplace.html
[aicssegmentation.core.vessel.vesselness2D]: https://allencell.github.io/aics-segmentation/aicssegmentation.core.html
