
[![License BSD-3](https://img.shields.io/pypi/l/cochlea-synapseg.svg?color=green)](https://github.com/ucsdmanorlab/cochlea-synapseg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/cochlea-synapseg.svg?color=green)](https://pypi.org/project/cochlea-synapseg)
[![Python Version](https://img.shields.io/pypi/pyversions/cochlea-synapseg.svg?color=green)](https://python.org)
[![tests](https://github.com/ucsdmanorlab/cochlea-synapseg/workflows/tests/badge.svg)](https://github.com/ucsdmanorlab/cochlea-synapseg/actions)
[![codecov](https://codecov.io/gh/ucsdmanorlab/cochlea-synapseg/branch/main/graph/badge.svg)](https://codecov.io/gh/ucsdmanorlab/cochlea-synapseg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/cochlea-synapseg)](https://napari-hub.org/plugins/cochlea-synapseg)

A plugin to segment cochlear ribbon synapses. 

More is in the works, but for now it includes tools to more quickly generate ground truth ribbon segmentation (Plugins > SynapSeg - Ground Truth Widget).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `cochlea-synapseg` (receommended: in a new conda environment with up-to-date napari) via [pip]:

    python -m pip install cochlea-synapseg

## Usage

After successfull installation, you can find the plugin next time you launch napari (Plugins > SynapSeg - Ground Truth Widget).

The ground truth widget is divided into multiple sections, for "quick use", be sure to check the settings denoted with asterisks:

### Image Tools

![image_tools](https://github.com/user-attachments/assets/323984ad-2cd3-4816-8ee5-e8b3f5063bc0)

\***1. Image Layer Selection** - use the dropdown to select the name of your image layer (here, the layer that contains the ribbon stain)

(First load a 3D image using one of napari's native readers, or using the Cochlea-Synapseg .zarr reader (reads a .zarr with '3d/raw' and '3d/labeled').)

\***2. Refresh Image Layer Selection** - update the list of available image layers in #1

**3. Pixel size information** - (in microns), used for some point readers to successfully convert real units to pixel coordinates. Can be left as 1 if this functionality is not needed.

**4. Split channels** - splits multiple channels into separate image layers (useful for FIJI-saved .tif images)

### Points Tools & Points to Labels

![points_tools](https://github.com/user-attachments/assets/6b271d5c-51c1-4ca4-b3c0-683dddd69dc8)

**5. Points Layer Selection and Refresh** - use the dropdown to select an existing points layer, use the refresh button to update the list (or skip to #8 if not loading in existing points)

**6. Real -> Pixel Units** - if you've loaded some points were saved in real units, make sure the pixel size information above in #3 is correct, then click "real -> pixel units"

**7. Channel Adjustment** - some points (like ImageJ/FIJI rois or CellCounter points), show up in the wrong z plane because their "slice" coordinates are a combination of both slice and channel info. If this happens, set the number of channels (in the original image, where the ROIs were created!), and then click "chan -> z convert". Z coordinates of the points layer will be divided by the number of channels specified. 

\***8. New Points Layer** - if starting annotation from scratch, click to create a new points layer. #5 should automatically select this new layer. 

\***9. Rotate to XY and \*10. Auto-adjust Z** - these convenient functions allow you to quickly annotate points in Napari's 3D view. Simply click "Rotate to XY before adding new points. These points will now have the correct XY position but will have missing Z information. (Rotate out of XY to confirm.) Click "Auto-adjust z" and the z will automatically adjust to the brightest point. 

**11. Manually Edit Z** - useful for overlapping points, can be used to manually edit the z position of ONLY selected points. Use the +/- arrow keys for single z steps type in a number to move a larger amount. 

**12. Snap too Max** - will automatically adjust all points to their local max (search radius defined in pixels in Advanced Settings -> snap to max rad). Useful for adjusting quickly dropped points, but proceed with caution if you have close-together points. 

\***13. Points to Labels** - the key functionality of the module, creates a label layer by performing a local segmentation on all points.

**14. Advanced Settings** - adjust settings for the points to labels function to optimize local segmentation and watershed separation of points. 

### Labels Tools

![labels_tools](https://github.com/user-attachments/assets/6ef20ff6-61e2-4337-a177-8f957a67fb39)

**15. Lables Layer Selection and Refresh** - use the dropdown to select an existing labels layer, use the refresh button to update the list

**16. Make Labels Editable** - zarrs and other file formats tend to load in as dask arrays, which don't allow editing. Checking this box will make the labels layer editable by converting to a numpy array (will load the layer into memory, so be careful if dealing with large images!). This will allow you to edit the labels layer with tools like the paintbrush and eraser. Automatically enables if merging or removing labels is requested (see #17 and #19)

\***17. Remove a Label** - use the labels layer eyedropper tool to identify the ID of an unwanted label, then type in the box and click "Remove label"

**18. Max Label Display** - shows the current maximum label ID. If you're painting labels by hand and need a new label ID, increment above this number. Use the refresh button to the right to get an up-to-date number if you've made changes to your label layer.

\***19. Merge labels** - if you have an existing labels layer, and then create new labels (e.g. from the points to labels function), select the layer you'd like to merge into your existing labels layer (i.e. box 15 and 19a should be different from one another!), and then click "merge labels". This function will automatically ensure overlapping label IDs are not used. 

**20. Labels to Points** - if wanted, you can take all your existing labels and convert them to a points layer based on their centroids. This may be helpful for quickly generating better labels using the points tools above. 

### Save to Zarr

![save_zarr](https://github.com/user-attachments/assets/1d824f49-012f-4fac-8fa1-64d7d319cd34)

Functionality to save to .zarr format. Saves image as '3d/raw' and labels as '3d/labeled'. Used for later auto-segmentation of ribbons (not live in this plugin yet, but coming soon!). 

\***21. File Path** - the directory in which to save the zarr; use the folder icon to search for an existing directory

\***22. File Name** - the zarr name to save to; use the magnifying glass icon to select an existing .zarr

**23. From Source** - set the file path and name to where the image layer was loaded from. (Caution: if you loaded a zarr, this will result in the zarr being overwritten!)

\***24. Save 3D Only (recommended)** - saves the image and labels layers (selected in #1 and #15) in the specified .zarr, as 3d/raw and 3d/labeled, respectively. A reader is included with this plugin for this format as well. 

**25. Save 2D and 3D** - (not recommended) to be used in the future if 2D models are to be run on the data, saves both the 3D stacks as in 24, and then individual 2D slices for each z in 2d/raw/[z] and 2d/labeled/[z]



## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"cochlea-synapseg" is free and open source software

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
