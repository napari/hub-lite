
[![License MIT](https://img.shields.io/pypi/l/napari-GapSeq2.svg?color=green)](https://github.com/piedrro/napari-PixSeq/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-GapSeq2.svg?color=green)](https://pypi.org/project/napari-PixSeq/)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-GapSeq2.svg?color=green)](https://python.org)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-GapSeq2)](https://napari-hub.org/plugins/napari-PixSeq)

A **Napari** plugin for extracting time series traces from single molecule FRET data.

napari-PixSeq uses **Picasso** (picassosr) as a backend and includes features for **aligning** image channels/datasets, **undrifting** images, **detecting/fitting** localisations and extracting **traces**, and supports both **ALEX** and **FRET** data. Traces can be exported in different formats for downstream analysis.

napari-PixSeq traces can be analysed with TraceAnalyser: https://github.com/piedrro/TraceAnalyser

This is still undergoing development, so some features may not work as expected.

This was built by Dr Piers Turner from the Kapanidis Lab, University of Oxford.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-PixSeq` via [pip]:

    pip install napari-PixSeq

You can install `napari-PixSeq` via [GitHub]:

    conda create –-name napari-pixseq python==3.9
    conda activate napari-pixseq
    conda install -c anaconda git
    conda update --all

    pip install git+https://github.com/piedrro/napari-PixSeq.git

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-PixSeq" is free and open source software

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

[file an issue]: https://github.com/piedrro/napari-GapSeq2/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
