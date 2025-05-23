
[![License](https://img.shields.io/pypi/l/napari-labelprop.svg?color=green)](https://github.com/nathandecaux/napari-labelprop/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-labelprop.svg?color=green)](https://pypi.org/project/napari-labelprop)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-labelprop.svg?color=green)](https://python.org)
[![tests](https://github.com/nathandecaux/napari-labelprop/workflows/tests/badge.svg)](https://github.com/nathandecaux/napari-labelprop/actions)
[![codecov](https://codecov.io/gh/nathandecaux/napari-labelprop/branch/main/graph/badge.svg)](https://codecov.io/gh/nathandecaux/napari-labelprop)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-labelprop)](https://napari-hub.org/plugins/napari-labelprop)



3D semi-automatic segmentation using deep registration-based 2D label propagation
---------------------------------------------------------------------------------
---

This [napari][napari] plugin was generated with [Cookiecutter][Cookiecutter] using [@napari][@napari]'s [cookiecutter-napari-plugin][cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## About

See "Semi-automatic muscle segmentation in MR images using deep registration-based label propagation" paper : 

[[Paper]![Paper](https://www.integrad.nl/assets/uploads/2016/02/cta-elsevier_logo-no_bg.png)](https://www.sciencedirect.com/science/article/pii/S0031320323002297?casa_token=r5FPBVXYXX4AAAAA:mStyUXb0i4lGqBmfF1j5fV1T9FuCMrpYfwh3lwQve2XAnzUBPZviAiFgMtH7lv6hdcWsA7yM) [[PDF]![PDF](https://www.ouvrirlascience.fr/wp-content/uploads/2018/12/HAL-3.png)](https://hal.science/hal-03945559/document)
<p>
  <img src="https://github.com/nathandecaux/labelprop.github.io/raw/main/demo_cut.gif" width="600">
</p>

## Installation

To install this project :

    pip install napari['all']
    pip install git+https://github.com/nathandecaux/napari-labelprop.git

## Usage

Download [pretrained weights](https://raw.githubusercontent.com/nathandecaux/napari-labelprop/main/pretrained.ckpt).

Open napari from terminal and start using functions from 'napari-labelprop' plugin (Under Plugins scrolling menu).

Available functions are :

- Inference : Propagate labels from trained weights (Pytorch checkpoint required)
- Training : Start training from scratch or from the pretrained weights.

PS : "Unsupervised pretraining" is not yet implemented. See CLI option at [LabelProp](https://github.com/nathandecaux/labelprop) repository.

Every operation is done in the main thread. So, napari is not responsive during training or inference, but you can still follow the progress in the terminal.

##### Training

To train a model, reach the plugin in the menu bar :

    Plugins > napari-labelprop > Training

Fill the fields with the following information :

- `Image` : Select a loaded napari.layers.Image layer to segment
- `Labels` : Select a loaded napari.layers.Labels layer with the initial labels
- `hints` : Select a loaded napari.layers.Labels layer with scribbled pseudo labels
- `Pretrained checkpoint` : Select a pretrained checkpoint from the server-side checkpoint directory
- `Slices shape` : Slices are resample to this shape for training and inference, then resampled to original shape. So far, slices must be squares.  
- `Propagation axis` : Set the axis to use for the propagation dimension
- `Max epochs` : Set the maximum number of epochs to train the model
- `Checkpoint output directory`
- `Checkpoint name`
- `Weighting criteria` : Defines the criteria used to weight each direction of propagation `ncc = normalized cross correlation (slow but smooth), distance = distance to the nearest label (fast but less accurate)`
- `Reduction` : When using ncc, defines the reduction to apply to the ncc map `mean / local_mean / none`. Default is `none`
- `Use GPU` : Set if whether to use the GPU or not. Default is `True` (GPU). GPU:0 is used by default. To use another GPU, set the `CUDA_VISIBLE_DEVICES` environment variable before launching napari.

##### Inference

To run inference on a model, reach the plugin in the menu bar :

    Plugins > napari-labelprop-remote > Inference

Fill the fields like in the training section. Then, click on the `Run` button.

## Contributing

Contributions are very welcome. Tests can be run with [tox][tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3][BSD-3] license,
"napari-labelprop" is free and open source software

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
