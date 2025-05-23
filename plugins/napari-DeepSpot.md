
[![License](https://img.shields.io/pypi/l/napari-DeepSpot.svg?color=green)](https://github.com/ebouilhol/napari-DeepSpot/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-DeepSpot.svg?color=green)](https://pypi.org/project/napari-DeepSpot)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-DeepSpot.svg?color=green)](https://python.org)
[![tests](https://github.com/ebouilhol/napari-DeepSpot/workflows/tests/badge.svg)](https://github.com/ebouilhol/napari-DeepSpot/actions)
[![codecov](https://codecov.io/gh/ebouilhol/napari-DeepSpot/branch/main/graph/badge.svg)](https://codecov.io/gh/ebouilhol/napari-DeepSpot)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-DeepSpot)](https://napari-hub.org/plugins/napari-DeepSpot)

RNA spot enhancement for fluorescent microscopy images.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-DeepSpot` via [pip]:

    pip install napari-DeepSpot

## Build from source

This plugin is using Tensorflow, make sure your Python environment has Tensorflow, on create a new environment using the following commands:
* Conda:  
`conda env create -f environment.yml`  
`conda activate deepspot-napari`
* Or pip:   
`pip install -r requirements.txt`

## Usage

Open one or multiple images using Napari GUI : 
File > Open > Select your image

The images are then displayed on Napari

Load the Plugin:
Plugins > Napari-DeepSpot:Enhance Spot

![Usage](./image/napari.png)

Click on the right panel Button "Enhance"

Wait a few seconds for the magic to happen :

![Usage](./image/napari_enhance.png)

You can see the original images and the enhanced version in the left panel in the layer section.

To save the images : File > Save all layers or File > Save selected layers.


![Usage](./image/napari_video.gif)



## Citation
If you use this plugin please cite the [paper](https://www.biorxiv.org/content/10.1101/2021.11.25.469984v1):

>@article {Bouilhol2021DeepSpot,  
>	 author = {Bouilhol, Emmanuel and Lefevre, Edgar and Dartigues, Benjamin and Brackin, Robyn and Savulescu, Anca Flavia and Nikolski, Macha},  
>	 title = {DeepSpot: a deep neural network for RNA spot enhancement in smFISH microscopy images},  
>	 elocation-id = {2021.11.25.469984},  
>	 year = {2021},  
>	 doi = {10.1101/2021.11.25.469984},  
>	 publisher = {Cold Spring Harbor Laboratory},  
>	 URL = {https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469984},  
>	 eprint = {https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469984.full.pdf},  
>	 journal = {bioRxiv}  
>}  

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-DeepSpot" is free and open source software

## Known Issues

If you have troubles with the Python packages `typing extensions`, use the command :  
`pip install typing-extensions --upgrade`  

When using "Enhance" on multiple images, Napari may freeze. Just wait until it comes to life again, the images will still be enhanced. This is due to Napari memory usage and will be fix one day.


## Other Issues

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

[file an issue]: https://github.com/ebouilhol/napari-DeepSpot/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/


