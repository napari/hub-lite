![microlink-logo-update](https://user-images.githubusercontent.com/17855764/146078168-dd557089-ff10-46d6-b24d-268f5d21a9ee.png)

[![License](https://img.shields.io/pypi/l/napari-imsmicrolink.svg?color=green)](https://github.com/nhpatterson/napari-imsmicrolink/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-imsmicrolink.svg?color=green)](https://pypi.org/project/napari-imsmicrolink)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-imsmicrolink.svg?color=green)](https://python.org)
[![tests](https://github.com/nhpatterson/napari-imsmicrolink/workflows/tests/badge.svg)](https://github.com/nhpatterson/napari-imsmicrolink/actions)

[napari] plugin to perform MALDI IMS - microscopy registration using laser ablation marks as described in [Anal. Chem. 2018, 90, 21, 12395–12403](https://pubs.acs.org/doi/abs/10.1021/acs.analchem.8b02884). This plugin is a work-in-progress but is mostly functional.

__N.B.__ This tool is __NOT__ a general purpose registration framework to find transforms between IMS (MALDI or otherwise)
and microscopy. It is built to align MALDI IMS pixels to their corresponding laser ablation marks as captured by microscopy AFTER the IMS experiment. 
This approach has the advantage of providing direct evidence of registration performance as IMS pixels are aligned 
to their _explicit spatial origin_ in microscopy space, improving overall accuracy and confidence of microscopy-driven IMS 
data analysis.

## Installation

You can install `napari-imsmicrolink` via [pip]:

    pip install napari-imsmicrolink

### Typical experiment workflow
1. Acquire pre-IMS microscopy (autofluorescence, brightfield) - _optional_
2. Perform normal IMS sample preparation.
3. Acquire post-IMS microscopy (autofluorescence, brightfield) with matrix still on sample
that reveals laser ablation marks.

4. Gather IMS data that contains XY integer coordinates for the IMS experiment
   (.imzML, Bruker spotlist (.txt, .csv), Bruker peaks.sqlite (_FTICR_),
   Bruker .tsf (TIMS qTOF only))

5. Run `napari-imsmicrolink` with data 3 and 4

6. Once registered, use `wsireg` to align other microscopy modalities to IMS-registered post-IMS
microscopy

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-imsmicrolink" is free and open source software

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
[file an issue]: https://github.com/nhpatterson/napari-imsmicrolink/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
