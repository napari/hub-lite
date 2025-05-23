
[![License](https://img.shields.io/pypi/l/arcos-gui.svg?color=green)](https://github.com/pertzlab/pertzlab/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/arcos-gui.svg)](https://pypi.org/project/arcos-gui)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/arcos-gui)](https://anaconda.org/conda-forge/arcos-gui)
[![Python Version](https://img.shields.io/pypi/pyversions/arcos-gui.svg?color=green?)](https://python.org)
[![tests](https://github.com/pertzlab/arcos-gui/workflows/tests/badge.svg)](https://github.com/pertzlab/arcos-gui/actions)
[![codecov](https://codecov.io/gh/pertzlab/arcos-gui/branch/main/graph/badge.svg)](https://codecov.io/gh/pertzlab/arcos-gui)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/arcos-gui)](https://napari-hub.org/plugins/arcos-gui)

A napari plugin to detect and visualize collective signaling events

----------------------------------
- Package specific Documentation: <https://pertzlab.github.io/arcos-gui>
- ARCOS documentation: <https://arcos.gitbook.io>

**A**utomated **R**ecognition of **C**ollective **S**ignalling (ARCOS) is an algorithm to identify collective spatial events in time series data.
It is available as an [R (ARCOS)](https://github.com/pertzlab/ARCOS) and [python (arcos4py)](https://github.com/pertzlab/arcos4py) package.
ARCOS can identify and visualize collective protein activation in 2- and 3D cell cultures over time.

This plugin integrates ARCOS into napari. Users can import tracked time-series data in CSV format or load data from napari-layer properties (such as the ones generated with [napari-skimage-regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops). The plugin
provides GUI elements to process this data with ARCOS. Layers containing the detected collective events are subsequently added to the viewer.

Following analysis, the user can export the output as a CSV file with the detected collective events or as a sequence of images to generate a movie.


![](https://github.com/bgraedel/arcos-gui/assets/100028238/66fa2afa-6f24-4cce-b29e-4279066c6c25)

[Watch full demo on youtube](https://www.youtube.com/watch?v=hG_z_BFcAiQ) (older plugin version)


# Installation

You can install `arcos-gui` via [pip]:

    pip install arcos-gui

Or via [conda-forge]:

    conda install -c conda-forge arcos-gui

## Usage

The plugin can be started from the napari menu `Plugins > ARCOS GUI`.
For detailed instructions on how to use the plugin, please refer to the [Usage section of the documentation](https://pertzlab.github.io/arcos-gui/Usage).

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.
See the [Contributing Guide](https://pertzlab.github.io/arcos-gui/Contributing) for more information.

## License

Distributed under the terms of the [BSD-3] license,
"arcos-gui" is free and open-source software

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

[file an issue]: https://github.com/pertzlab/arcos-gui/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/arcos-gui/
[conda-forge]: https://anaconda.org/conda-forge/arcos-gui
[PyPI]: https://pypi.org/

## Credits
We were able to develop this plugin in part due to funding from the [CZI napari Plugin Foundation Grant](https://chanzuckerberg.com/science/programs-resources/imaging/napari/detecting-and-quantifying-space-time-correlations-in-cell-signaling/).

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Citation

If you use this plugin in your research, please cite the following [paper](https://doi.org/10.1083/jcb.202207048):

    @article{10.1083/jcb.202207048,
        author = {Gagliardi, Paolo Armando and Grädel, Benjamin and Jacques, Marc-Antoine and Hinderling, Lucien and Ender, Pascal and Cohen, Andrew R. and Kastberger, Gerald and Pertz, Olivier and Dobrzyński, Maciej},
        title = "{Automatic detection of spatio-temporal signaling patterns in cell collectives}",
        journal = {Journal of Cell Biology},
        volume = {222},
        number = {10},
        pages = {e202207048},
        year = {2023},
        month = {07},
        abstract = "{Increasing experimental evidence points to the physiological importance of space–time correlations in signaling of cell collectives. From wound healing to epithelial homeostasis to morphogenesis, coordinated activation of biomolecules between cells allows the collectives to perform more complex tasks and to better tackle environmental challenges. To capture this information exchange and to advance new theories of emergent phenomena, we created ARCOS, a computational method to detect and quantify collective signaling. We demonstrate ARCOS on cell and organism collectives with space–time correlations on different scales in 2D and 3D. We made a new observation that oncogenic mutations in the MAPK/ERK and PIK3CA/Akt pathways of MCF10A epithelial cells hyperstimulate intercellular ERK activity waves that are largely dependent on matrix metalloproteinase intercellular signaling. ARCOS is open-source and available as R and Python packages. It also includes a plugin for the napari image viewer to interactively quantify collective phenomena without prior programming experience.}",
        issn = {0021-9525},
        doi = {10.1083/jcb.202207048},
        url = {https://doi.org/10.1083/jcb.202207048},
        eprint = {https://rupress.org/jcb/article-pdf/222/10/e202207048/1915749/jcb/_202207048.pdf},
    }
