
[![License BSD-3](https://img.shields.io/pypi/l/frontveg.svg?color=green)](https://github.com/hereariim/frontveg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/frontveg.svg?color=green)](https://pypi.org/project/frontveg)
[![Python Version](https://img.shields.io/pypi/pyversions/frontveg.svg?color=green)](https://python.org)
[![tests](https://github.com/hereariim/frontveg/workflows/tests/badge.svg)](https://github.com/hereariim/frontveg/actions)
[![codecov](https://codecov.io/gh/hereariim/frontveg/branch/main/graph/badge.svg)](https://codecov.io/gh/hereariim/frontveg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/frontveg)](https://napari-hub.org/plugins/frontveg)
[![npe2](https://img.shields.io/badge/plugin-npe2-blue?link=https://napari.org/stable/plugins/index.html)](https://napari.org/stable/plugins/index.html)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)

A plugin for foreground vegetation segmentation, tailored for trellised vegetation row images. It uses RGB images to perform inference and allows users to manually refine the generated mask.

----------------------------------

The method was developped by Herearii Metuarea, PHENET PhD at LARIS (French laboratory located in Angers, France) and Abdoul-Djalil Hamza Ousseini, AgroEcoPhen Engineer at IRHS (French Institute located in INRAe Angers, France) in Imhorphen team (bioimaging research group lead) under the supervision of Eric Duchêne (Research Engineer), Morgane Roth (Research Engineer) and David Rousseau (Full professor). This plugin was written by Herearii Metuarea and was designed in the context of the european project PHENET.

![Data Warehouse](https://github.com/user-attachments/assets/4a110408-5854-4e8c-b655-4cb588434b79)


----------------------------------

This [napari] plugin was generated with [copier] using the [napari-plugin-template].

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/napari-plugin-template#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `frontveg` via [pip]:

    pip install frontveg



To install latest development version :

    pip install git+https://github.com/hereariim/frontveg.git

## Description

This plugin is a tool to perform image inference. This plugin contained two steps of image processing. First, from RGB image, an depth map is estimated and then thresholded to detect foreground and background in image. Second, grounding dino model detect foliage in foreground. The output is a binary mask where white colour are associated to foliage in foreground.

The plugin is applicable to images of trellised plants; in this configuration, it has been applied to images of pome fruit trees (apple), stone fruit trees (abricot) and climbing plants (grapevine).

![sample_example](https://github.com/user-attachments/assets/ae845e01-9f48-4bcf-98ad-bf5f6e037f01)

## Contact

Imhorphen team, bioimaging research group

42 rue George Morel, Angers, France

- Pr David Rousseau, david.rousseau@univ-angers.fr
- Abdoul-djalil ousseini-hamza, abdoul-djalil.ousseini-hamza@inrae.fr
- Herearii Metuarea, herearii.metuarea@univ-angers.fr

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"frontveg" is free and open source software

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

[file an issue]: https://github.com/hereariim/frontveg/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
