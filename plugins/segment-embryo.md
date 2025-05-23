
[![License MIT](https://img.shields.io/pypi/l/segment-embryo.svg?color=green)](https://github.com/MontpellierRessourcesImagerie/segment-embryo/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/segment-embryo.svg?color=green)](https://pypi.org/project/segment-embryo)
[![Python Version](https://img.shields.io/pypi/pyversions/segment-embryo.svg?color=green)](https://python.org)
[![tests](https://github.com/MontpellierRessourcesImagerie/segment-embryo/workflows/tests/badge.svg)](https://github.com/MontpellierRessourcesImagerie/segment-embryo/actions)
[![codecov](https://codecov.io/gh/MontpellierRessourcesImagerie/segment-embryo/branch/main/graph/badge.svg)](https://codecov.io/gh/MontpellierRessourcesImagerie/segment-embryo)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/segment-embryo)](https://napari-hub.org/plugins/segment-embryo)

<img src="https://github.com/user-attachments/assets/4459f48c-435f-489d-b27c-25a4ea390871" align='left' width="30%"></img> 3D Segment ascidian embryos using cellpose. The images are first rescaled to be isotropic and then downscaled, before cellpose is used. The resulting labels are upscaled to match the original data.

----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `segment-embryo` via [pip]:

    pip install segment-embryo

## Usage

We will segment the cells of an embryo and count the mRNA spots tagged in another channel per cell.

### 1. Opening an image

Drag a tif- or czi-file from your file-browser and drop it into the napari window. The image will opened. The napari-plugin [napari-czifile2](https://github.com/BodenmillerGroup/napari-czifile2) is used to open czi-files.

### 2. Checking and modifying the voxel size 

Open the plugin [Scale-Tool plugin](https://pypi.org/project/set-calibration/) from the ``Plugins``-menu. Make sure the voxel-size values are set correctly in nm. Correct the values and the unit if necessary and press the ``Apply to all`` button.

<img src="https://github.com/user-attachments/assets/409b669b-675f-495f-ba11-c6ded0442b2b" align='left' width="30%"></img> 

### 3. Segmenting the cells of the embryo

<img src="https://github.com/user-attachments/assets/1b464f39-47ff-412d-bdb8-c2d61837af39" align='right' width="30%"></img> 

Close the [Scale-Tool plugin](https://pypi.org/project/set-calibration/) and open the ``Embryo Segmentation``-plugin from the ``Plugins``-menu. Select the layer containing the membranes as ``input image`` and the layer containing the nuclei as ``nuclei image``. Press the ``run`` button and wait until the segmentation is finished. When the segmentation is finished a ``Labels layer`` with the result will be added to the layers list. 

<img src="https://github.com/user-attachments/assets/4dcf8aad-22ef-4a20-a6a6-50bcb81c7011" align='left' width="20%"></img> 

### 4. Exporting and curating the labels

If the labels need curation, select  the labels layer and save it to a tiff-file via the menu ``File>Save Selected Layers...``. Import the saved labels into the [Morphonet 2 standalone client](https://morphonet.org/downloads), make the corrrections and export the corrected labels to a tiff-file. Open the tiff-file in napari.

### 5. Detecting spots

Close the ``Embryo Segmentation`` plugin, select the layer containing the mRNA-spots and open the [Detect FISH spots-plugin](https://www.napari-hub.org/plugins/napari-bigfish) from the ``Plugins``-menu. Estimate the spot size in xy and z in ImageJ and enter the values into the corresponding fields. You can either estimate the threshold let the software find a threshold value. Press the ``detect spots button``. Depending on the result you might want to modify the threshold-value and run the plugin again.

<img src="https://github.com/user-attachments/assets/6507eb3e-d732-4d69-8c63-02d83f8975f1" align='left' width="30%"></img> 

### 6. Counting Spots per cell

In the ``Spot Counting`` section of the plugin, select the spots layer as input and the labels layer for the ``cytoplasm labels`` and also for the ``nuclei labels``. 

![image](https://github.com/user-attachments/assets/445da47f-c3fc-4437-803d-e635500bf1af)

Press the ``Count Spots`` button! You will obtain a table with the numbers of spots per cell. If you provide the image twice, for the cytoplasm as well as for the nuclei, the spots will all be counted inside the nuclei. If you also want to know per cell how many spots are in the nucleus and how many are in the cytoplasm, you need to provide a mask or label image for the nuclei. You can obtain one by thresholding the nucleus image or by selecting ``segment nuclei`` in step 3.


<img src="https://github.com/user-attachments/assets/7f325bc5-baaf-4b74-b240-f174b81d0e96" align='left' width="30%"></img>
<img src="https://github.com/user-attachments/assets/463072c7-d647-4d23-90d9-15de3398bf31" align='right' width="30%"></img>

You can copy the data from the table to your spreadsheat software. Activate the table by clicking into it and press ``ctrl+a`` to select all rows and columns. Press ``ctrl+c`` to copy the data to the clipboard and ``ctrl+v`` to paste it into your spreadsheet.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"segment-embryo" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[copier]: https://copier.readthedocs.io/en/stable/
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[napari-plugin-template]: https://github.com/napari/napari-plugin-template

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
