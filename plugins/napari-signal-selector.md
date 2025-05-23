
[![License BSD-3](https://img.shields.io/pypi/l/napari-signal-selector.svg?color=green)](https://github.com/zoccoler/napari-signal-selector/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-signal-selector.svg?color=green)](https://pypi.org/project/napari-signal-selector)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-signal-selector.svg?color=green)](https://python.org)
[![tests](https://github.com/zoccoler/napari-signal-selector/workflows/tests/badge.svg)](https://github.com/zoccoler/napari-signal-selector/actions)
[![codecov](https://codecov.io/gh/zoccoler/napari-signal-selector/branch/main/graph/badge.svg)](https://codecov.io/gh/zoccoler/napari-signal-selector)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-signal-selector)](https://napari-hub.org/plugins/napari-signal-selector)
[![DOI](https://zenodo.org/badge/661588266.svg)](https://zenodo.org/doi/10.5281/zenodo.10041219)

An interactive signal selector and annotator for napari, based on [matplotlib](https://matplotlib.org/stable/).

[Jump to Intallation](#installation)

----------------------------------

## Usage

This plugin opens an embedded plotter in napari capable of plotting and interacting (selecting/annotating) with individual object signals (typically temporal features).

![plotting](https://github.com/zoccoler/napari-signal-selector/raw/main/images/plotting.gif)

### Input Data

napari-signal-selector works with a [Labels layer](https://napari.org/stable/howtos/layers/labels.html) containing segmented objects and whose `features` attribute contains a table that follows the example structure shown below:

| `label` | `frame` | `feature` | ...  |
|-------|-------|---------|---|
| 1     | 0     | 1.0     | ...  |
| 2     | 0     | 1.0     | ...  |
| 3     | 0     | 0.5     | ...  |
| 4     | 0     | 0.5     | ...  |
| 1     | 1     | 2.0     | ...  |
| 2     | 1     | 1.0     | ...  |
| 3     | 1     | 1.0     | ...  |
| 4     | 1     | 1.0     | ...  |
| 1     | 2     | 3.0     | ...  |
| 2     | 2     | 1.0     | ...  |
| 3     | 2     | 0.5     | ...  |
| 4     | 2     | 1.5     | ...  |
| ⋮     | ⋮     | ⋮     |   |

Basically, it needs an object identifier (in this case, the `label` column) that matches the labels in the Labels layer, and other columns containing x- and y-axis numbers to plot. Typically, x-axis is some temporal-related property.

Here is how one could add such a layer to a napari viewer via code (check [this example notebook](./examples/synthetic_example.ipynb) for more details):

```python
viewer.add_labels(labels_image, features = table)
```

If a layer like this is selected, you can choose what to plot by means of dropdown fields in the bottom of the plotter.

Below is a basic example using the "Flashing Polygons" synthetic data:

![intro](https://github.com/zoccoler/napari-signal-selector/raw/main/images/intro.gif)

## Tools

### Selection Tool

The selection tool (arrowhead icon) is a toggle button which enables you to select individual signals. Once activated, the icon gets highlighted and you can click over individual signals to select them. Right-clicking unselects everything.

![select](https://github.com/zoccoler/napari-signal-selector/raw/main/images/select.gif)

If the region you want to click is too crowded, consider zooming in first and then selecting.

![zoom-select](https://github.com/zoccoler/napari-signal-selector/raw/main/images/zoom_select.gif)

And if you know which label you want to select, you can enable `'show selected'` from the Labels layer options to solely display one label at a time. The Lables layer picker tool may help you get the right label.

![show-selected](https://github.com/zoccoler/napari-signal-selector/raw/main/images/show_selected.gif)

### Annotation Tool

Once one or multiple signals are selected, you can annotate them with the annotation tool (brush with a 'plus' icon). You need to choose a signal class first.
*Remember to right-click to remove previous selections when annotating different signal classes!*

![annotation](https://github.com/zoccoler/napari-signal-selector/raw/main/images/annotation.gif)

Annotations are saved back in the table in a new column called 'Annotations'.
*Currently multiple annotations is not possible, i.e., more than one class assigned to the same part of the signal.*

### Span-Selection Tool

You can use the span-selection tool (bounded horizontal arrows icon) to sub-select one or multiple parts of signals. Right-click to unselect regions. Hold 'SHIFT' while dragging the mouse to select multiple sub-regions.

![span-select](https://github.com/zoccoler/napari-signal-selector/raw/main/images/span_select.gif)

You can use this in conjunction with the annotation tool to have sub-regions from the same signal with different annotations.

![](https://github.com/zoccoler/napari-signal-selector/raw/main/images/span_annotation.gif)

### Deletion Tool

If you made a mistake, you can remove previous annotations by selecting signal(s) and clicking on the trash icon at the right of the toolbar (or just annotate them with class 0).

![delete](https://github.com/zoccoler/napari-signal-selector/raw/main/images/delete.gif)

Also, with the selection tool enbaled, by holding 'SHIFT' and left-clicking, you can select all signals. This may be useful to delete all previous annotations.

![select-delete-all](https://github.com/zoccoler/napari-signal-selector/raw/main/images/select_delete_all.gif)

### Exporting Annotations

The table with annotations can be displayed in napari using the 'Show table' widget from [napari-skimage-regionprops plugin](https://github.com/haesleinhuepf/napari-skimage-regionprops#napari-skimage-regionprops-nsr), which is available under `Tools > Measurements > Show Table (nsr)`. This plugin may require a specific napari version, so check its documentation for more details.

![](https://github.com/zoccoler/napari-signal-selector/raw/main/images/table_view.gif)

By the way, with `'show selected'` checked, you can click on a label row in the table and see the corresponding label in the image **...and** in the plotter!

To export the table, click on `'Save as csv...'`.

Another option is to run the following code in the napari console (replace `'Labels'` with the name of your Labels layer and `'annotations.csv'` with the desired file name or file path):

```python
import pandas as pd
df = viewer.layers['Labels'].data.features
df.to_csv('annotations.csv')
```

## Installation

You can install `napari-signal-selector` via [pip]. Follow these steps from a terminal.

We recommend using `mamba-forge` whenever possible. Click [here](https://github.com/conda-forge/miniforge#mambaforge) to choose the right download option for your OS.
**If you do not use `mamba-forge`, replace the `mamba` term whenever you see it below with `conda`.**

Create a conda environment :

    mamba create -n napari-ss-env napari pyqt python=3.9
    
Activate the environment :

    mamba activate napari-ss-env

Install `napari-signal-selector` via [pip] :

    pip install napari-signal-selector

Alternatively, install latest development version with :

    pip install git+https://github.com/zoccoler/napari-signal-selector.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-signal-selector" is free and open source software

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

[file an issue]: https://github.com/zoccoler/napari-signal-selector/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
