    # napari-svetlana

[![License](https://img.shields.io/pypi/l/napari_svetlana.svg?color=green)](https://bitbucket.org/koopa31/napari_svetlana/src/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari_svetlana.svg?color=green)](https://pypi.org/project/napari_svetlana)
[![Python Version](https://img.shields.io/pypi/pyversions/napari_svetlana.svg?color=green)](https://python.org)
[![tests](https://bitbucket.org/koopa31/napari_svetlana/workflows/tests/badge.svg)](https://bitbucket.org/koopa31/napari_svetlana/actions)
[![codecov](https://codecov.io/gh/koopa31/napari_svetlana/branch/main/graph/badge.svg)](https://codecov.io/gh/koopa31/napari_svetlana)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-svetlana)](https://napari-hub.org/plugins/napari-svetlana)
[![Documentation](https://readthedocs.org/projects/svetlana-documentation/badge/?version=latest)](https://svetlana-documentation.readthedocs.io/en/latest/)

The aim of this plugin is to classify the output of a segmentation algorithm.
The inputs are :
<ul>
  <li>A folder of raw images</li>
  <li>Their segmentation masks where each ROI has its own label.</li>
</ul>

Svetlana can process 2D, 3D and multichannel image. If you want to use it to work on cell images, we strongly
recommend the use of [Cellpose](https://www.cellpose.org) for the segmentation part, as it provides excellent quality results and a standard output format
accepted by Svetlana (labels masks). 

If you use this plugin please cite the [paper](https://www.nature.com/articles/s41598-024-60916-8): 

Cazorla, C., Weiss, P., & Morin, R. (2024). Svetlana: a Supervised Segmentation Classifier for Napari.

```bibtex
@article{cazorla2024svetlana,
  title={Svetlana a supervised segmentation classifier for Napari},
  author={Cazorla, Cl{\'e}ment and Morin, Renaud and Weiss, Pierre},
  journal={Scientific Reports},
  volume={14},
  number={1},
  pages={11604},
  year={2024},
  publisher={Nature Publishing Group UK London}
}

```


![](https://bitbucket.org/koopa31/napari_svetlana/raw/bca8788111b38d97bd172c7caac87cc488ace699/images/Videogif.gif)


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

First install Napari in a Python 3.9 Conda environment following these instructions :

```bash
conda create -n svetlana_env python=3.9
conda activate svetlana_env
conda install pip
python -m pip install "napari[all]"==0.4.17
```

Then, you can install `napari_svetlana` via [pip](https://pypi.org/project/napari-svetlana/), or directly from the Napari plugin manager (see Napari documentation):
```bash
pip install napari_svetlana
```
WARNING:

If you have a Cuda compatible GPU on your computer, some computations may be accelerated
using [Cupy](https://pypi.org/project/cupy/). Unfortunately, Cupy needs Cudatoolkit to be installed. This library can only be installed via 
Conda while the plugin is a pip plugin, so it must be installed manually for the moment:
```bash
conda install cudatoolkit=11.5 
```
Also note that the library ([Cucim](https://pypi.org/project/cucim/)) that we use to improve these performances, computing morphological operations on GPU
is unfortunately only available for Linux systems. Hence, if you are a Windows user, this installation is not necessary.

## Tutorial

Many advanced features are available in Svetlana, such as data augmentation or contextual information reduction, to optimize the performance of your classifier. Thus, we strongly encourage you to
check our [Youtube tutorial](https://www.youtube.com/watch?v=u_FKuHta-RE) and
our [documentation](https://svetlana-documentation.readthedocs.io/en/latest/).
A button called **TRY ON DEMO IMAGE** is available in the annotation plugin and enables you to apply the YouTube
tutorial to the same test images to learn how to use the plugin. Feel free to try it to test all the features
that Svetlana offers.

## Similar Napari plugins

Joel Luethi developed a similar method for objects classification called [napari feature classifier](https://www.napari-hub.org/plugins/napari-feature-classifier).
Also, [apoc](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification) by Robert Haase is available in Napari for pixels and objects classification.

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [BSD-3] license,
"napari_svetlana" is free and open source software

## Acknowledgements

The method was developed by [Clément Cazorla](https://koopa31.github.io/), [Renaud Morin](https://www.linkedin.com/in/renaud-morin-6a42665b/?originalSubdomain=fr) and [Pierre Weiss](https://www.math.univ-toulouse.fr/~weiss/). And the plugin was written by
Clément Cazorla. The project is co-funded by [Imactiv-3D](https://www.imactiv-3d.com/) and [CNRS](https://www.cnrs.fr/fr).

## Issues

If you encounter any problems, please [file an issue](https://bitbucket.org/koopa31/napari_svetlana/issues?status=new&status=open) along with a detailed description.

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
