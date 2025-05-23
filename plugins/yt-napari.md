
[![License](https://img.shields.io/pypi/l/yt-napari.svg?color=green)](https://github.com/data-exp-lab/yt-napari/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/yt-napari.svg?color=green)](https://pypi.org/project/yt-napari)
[![Python Version](https://img.shields.io/pypi/pyversions/yt-napari.svg?color=green)](https://python.org)
[![tests](https://github.com/data-exp-lab/yt-napari/workflows/tests/badge.svg)](https://github.com/data-exp-lab/yt-napari/actions)
[![codecov](https://codecov.io/gh/data-exp-lab/yt-napari/branch/main/graph/badge.svg)](https://codecov.io/gh/data-exp-lab/yt-napari)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/yt-napari)](https://napari-hub.org/plugins/yt-napari)
[![Documentation Status](https://readthedocs.org/projects/yt-napari/badge/?version=latest)](https://yt-napari.readthedocs.io/en/latest/?badge=latest)

A [napari] plugin for loading data from [yt].

This readme provides a brief overview including:

1. [Installation](#Installation)
2. [Quick Start](#Quick-Start)
3. [Contributing](#Contributing)

Full documentation is available at [yt-napari.readthedocs.io].

## Installation

### 1. (optional) install `yt` and `napari`

If you skip this step, the installation in the following section will only install the minimal package requirements for `yt` or `napari`, in which case you will likely need to manually install some packages. So if you are new to either package, or if you are installing in a clean environment, it may be simpler to  install these packages first.

For `napari`,

    pip install napari[all]

will install `napari` with the default `Qt` backend (see [here](https://napari.org/tutorials/fundamentals/installation#choosing-a-different-qt-backend) for how to choose between `PyQt5` or `PySide2`).

For `yt`, you will need `yt>=4.0.1` and any of the optional dependencies for your particular workflow. If you know that you'll need more than the base `yt` install, you can install the full suite of dependent packages with

    pip install yt[full]

See the [`yt` documentation](https://yt-project.org/doc/installing.html#leveraging-optional-yt-runtime-dependencies) for more information. If you're not sure which packages you'll need but don't want the full yt installation, you can proceed to the next step and then install any packages as needed (you will receive error messages when a required package is missing).

### 2. install `yt-napari`

You can install the `yt-napari` plugin with:

    pip install yt-napari

If you are missing either `yt` or `napari` (or they need to be updated), the above installation will fetch and run a minimal installation for both.

To install the latest development version of the plugin instead, use:

    pip install git+https://github.com/data-exp-lab/yt-napari.git

Note that if you are working off the development version, be sure to use the latest documentation
for reference: https://yt-napari.readthedocs.io/en/latest/

## Quick Start

After [installation](#Installation), there are three modes of using `yt-napari`:

1. jupyter notebook interaction ([jump down](#jupyter-notebook-interaction))
2. loading a json file from the napari gui ([jump down](#loading-a-json-file-from-the-napari-gui))
3. napari widget plugins ([jump down](#napari-widget-plugins))

### jupyter notebook interaction

`yt-napari` provides a helper class, `yt_napari.viewer.Scene` that assists in properly aligning new yt selections in the napari viewer when working in a Jupyter notebook.

```python
import napari
import yt
from yt_napari.viewer import Scene
from napari.utils import nbscreenshot

viewer = napari.Viewer()
ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")
yt_scene = Scene()

left_edge = ds.domain_center - ds.arr([40, 40, 40], 'kpc')
right_edge = ds.domain_center + ds.arr([40, 40, 40], 'kpc')
res = (600, 600, 600)

yt_scene.add_region(viewer,
                    ds,
                    ("enzo", "Temperature"),
                    left_edge=left_edge,
                    right_edge=right_edge,
                    resolution=res)

yt_scene.add_region(viewer,
                    ds,
                    ("enzo", "Density"),
                    left_edge=left_edge,
                    right_edge=right_edge,
                    resolution=res)

nbscreenshot(viewer)
```

 ![Loading a subset of a yt dataset in napari from a Jupyter notebook](./assets/images/readme_ex_001.png)

`yt_scene.add_to_viewer` accepts any of the keyword arguments allowed by `viewer.add_image`. See the full documentation ([yt-napari.readthedocs.io]) for more examples, including additional helper methods for linking layer appearance.

Additionally, with `yt_napari`>= v0.2.0, you can use the `yt_napari.timeseries` module to help sample and load in selections from across datasets.

### loading a selection from a yt dataset interactively

`yt-napari` provides two ways to sample a yt dataset and load in an image layer into a Napari viewer: the yt Reader plugin and json file specification.

#### using the yt Reader plugin

To use the yt Reader plugin, click on `Plugins -> yt-napari: yt Reader`. From there, add a region or slice selector then specify a field type and field and bounds to sample  between and then simply click "Load":

![Loading a subset of a yt dataset from the napari viewer](./assets/images/readme_ex_003_gui_reader.gif)

You can add multiple selections and load them all at once or adjust values and click "Load" again.

#### using the yt Time Series Reader plugin

To use the yt Time Series Reader plugin, click on  `Plugins -> yt-napari: yt Time Series Reader`. Specify your file matching: use `file_pattern` to enter glob expressions or use `file_list` to enter a list of specific files.
Then add a slice or region to sample for each matched dataset file (note: be careful of memory here!):

![Loading timeseries selections from the napari viewer](./assets/images/readme_ex_004_gui_timeseries.gif)

#### using a json file and schema

`yt-napari` also provides the ability to load json that contain specifications for loading a file. Properly formatted files can be loaded from the napari GUI as you would load any image file (`File->Open`). The json file describes the selection process for a dataset as described by a json-schema. The following json file results in similar layers as the above examples:


```json
{"$schema": "https://raw.githubusercontent.com/data-exp-lab/yt-napari/main/src/yt_napari/schemas/yt-napari_0.0.1.json",
 "datasets": [{"filename": "IsolatedGalaxy/galaxy0030/galaxy0030",
               "selections": {"regions": [{
                                "fields": [{"field_name": "Temperature", "field_type": "enzo", "take_log": true},
                                           {"field_name": "Density", "field_type": "enzo", "take_log": true}],
                                "left_edge": [460.0, 460.0, 460.0],
                                "right_edge": [560.0, 560.0, 560.0],
                                "resolution": [600, 600, 600]
                              }]},
               "edge_units": "kpc"
             }]
}
```

To help in filling out a json file, it is recommended that you use an editor capable of parsing a json schema and displaying hints. For example, in vscode, you will see field suggestions after specifying the `yt-napari` schema:

![interactive json completion for yt-napari](./assets/images/readme_ex_002_json.png)

See the full documentation at [yt-napari.readthedocs.io] for a complete specification.


## Contributing

Contributions are very welcome! Development follows a fork and pull request workflow. To get started, you'll need a development installation and a testing environment.

### development environment

To start developing, fork the repository and clone your fork to get a local copy. You can then install in development mode with

    pip install -e .

### tests and style checks

Both bug fixes and new features will need to pass the existing test suite and style checks. While both will be run automatically when you submit a pull request, it is helpful to run the test suites locally and run style checks throughout development. For testing, you can use [tox] to test different python versions on your platform.

    pip install tox

And then from the top level of the `yt-napari` directory, run

    tox

Tox will then run a series of tests in isolated environments. In addition to checking the terminal output for test results, the tox run will generate a test coverage report: a `coverage.xml` file and a `htmlcov` folder -- to view the results, open `htmlcov/index.html` in a browser.

If you prefer a lighter weight test, you can also use `pytest` directly and rely on the Github CI to test different python versions and systems. To do so, first install `pytest` and some related plugins:

    pip install pytest pytest-qt pytest-cov

Now, to run the tests:

    pytest -v --cov=yt_napari --cov-report=html

In addition to telling you whether or not the tests pass, the above command will write out a code coverage report to the `htmlcov` directory. You can open up `htmlcov/index.html` in a browser and check out the lines of code that were missed by existing tests.

For style checks, you can use [pre-commit](https://pre-commit.com/) to run checks as you develop. To set up `pre-commit`:

    pip install pre-commit
    pre-commit install

after which, every time you run `git commit`, some automatic style adjustments and checks will run. The same style checks will run when you submit a pull request, but it's often easier to catch them early.

After submitting a pull request, the `pre-commit.ci` bot will run the style checks. If style checks fail, you can have the bot attempt to auto-fix the failures by adding the following in a comment on it's own:

    pre-commit.ci autofix

The bot will then commit changes to your pull request after which you will want to run `git pull` locally to update your local version of the branch before making further changes to the branch.

### building documentation locally

Documentation can be built using `sphinx` in two steps. First, update the api mapping with

    sphinx-apidoc -f -o docs/source src/yt_napari/

This will update the `rst` files in `docs/source/` with the latest docstrings in `yt_napari`. Next, build the html documentation with

    make html


### updating the pydantic models and schema

The schema versioning follows a `major.minor.micro` versioning pattern that matches the yt-napari versioning. Each yt-napari release should have an accompanying updated schema file, even if the  contents of the schema file have not changed. On-disk schema are stored in  `src/yt_napari/schemas/`, with copies in the documentation at `docs/_static`.

There are a number of utilities to help automate the management of schema in `repo_utilities/`. The easiest way to use these utitities is with `taskipy` from the command line. To list available scripts:

```commandline
task --list
```

Before a release, run

```commandline
task validate_release vX.X.X
```

where `vX.X.X` is the version of the upcoming release. This script will run through some checks that ensure:
* the on-disk schema matches the schema generated by the pydantic model
* the schema files in the documentation match the schema files in the package

If any of the checks fail, you will be advised to update the schema using `update_schema_docs`. If you
run without providing a version:

```commandline
task update_schema_docs
```

It will simply copy over the existing on-disk schema files to the documentation. If you run with a version:

```commandline
task update_schema_docs -v vX.X.X
```
It will write a schema file for the current pydantic model, overwriting any on-disk schema files for
the provided version.

## License

Distributed under the terms of the [BSD-3] license,
"yt-napari" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## Funding

The yt-napari plugin project was funded with support from the Chan Zuckerberg Initiative through the napari Plugin Accelerator Grants project, [Enabling Access To Multi-resolution Data](https://chanzuckerberg.com/science/programs-resources/imaging/napari/enabling-access-to-multi-resolution-data/).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

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
[yt-napari.readthedocs.io]: https://yt-napari.readthedocs.io/en/stable/

[file an issue]: https://github.com/data-exp-lab/yt-napari/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[yt]: https://yt-project.org/
