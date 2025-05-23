
Napari plugin to use segment anything version 2.1 models from Meta.

Plugin made for segmenting 3d volumetric data or 3d time series data.

----------------------------------

## Installation

The plugin requires the following pre-requisite to be installed :

1. Python and pytorch versions

python>=3.10,torch>=2.5.1 and torchvision>=0.20.1 required

To install pytorch with your respective OS please visit - https://pytorch.org/get-started/locally/

2. SAM v2 installation from meta

Please refer https://github.com/facebookresearch/sam2

3. Install napari

python -m pip install "napari[all]"

Following is a sample conda environment installation with the above pre-req 

    conda create -n samv2_env python=3.10
    conda activate samv2_env
    pip3 install torch torchvision

    git clone https://github.com/facebookresearch/sam2.git && cd sam2
    pip install -e .

    python -m pip install "napari[all]"

    pip install napari-SAMV2


## Usage

Middle mouse click - positive point or keyboard shortcut "a"

Ctrl + Middle mouse click - negative point or keyboard shortcut "n"

Time Series Segmentation :

![samv2_time_series_demo](https://github.com/user-attachments/assets/078ca2bb-3016-4257-ac7c-c3cde8f9d125)



Volume Segmentation :

![samv2_volume_segmentation](https://github.com/user-attachments/assets/af05fcc4-a60d-44e8-ae05-70764d96e828)



Reference :

Example Data in the demo videos are from,

Cell tracking challenge - https://celltrackingchallenge.net/ 

and

FlyEM project - https://www.janelia.org/project-team/flyem/hemibrain


## License

Distributed under the terms of the [BSD-3] license,
"napari-SAMV2" is free and open source software



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

[file an issue]: https://github.com/Krishvraman/napari-SAMV2/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
