
[![License BSD-3](https://img.shields.io/pypi/l/napari-k2-WaveBreaker.svg?color=green)](https://github.com/SamKVs/napari-k2-WaveBreaker/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-k2-WaveBreaker.svg?color=green)](https://pypi.org/project/napari-k2-WaveBreaker)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-k2-WaveBreaker.svg?color=green)](https://python.org)
[![tests](https://github.com/SamKVs/napari-k2-WaveBreaker/workflows/tests/badge.svg)](https://github.com/SamKVs/napari-k2-WaveBreaker/actions)
[![codecov](https://codecov.io/gh/SamKVs/napari-k2-WaveBreaker/branch/main/graph/badge.svg)](https://codecov.io/gh/SamKVs/napari-k2-WaveBreaker)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-k2-WaveBreaker)](https://napari-hub.org/plugins/napari-k2-WaveBreaker)

<div>
    <img src="static/Logo.png">
</div>
<h2>About this plugin</h2>


This Napari plugin was designed for the detection and quantification of periodic biological structures.
As this plugin has not been uploaded to napari-hub as of this moment it **cannot be installed on a pre-compiled, bundled 
version of Napari**. Therefore Napari will need to be installed as a python package 
(<a href="https://napari.org/stable/tutorials/fundamentals/installation.html">more info about Napari installation</a>). 
Further information about the installation and licensing of the plugin can be found below. A detailed manual on the usage of the plugin can be found below as well. 

**If you have any questions or need help with the installation, please do hesitate to use the issues tab.**

**In case you need a tutorial on how to use the plugin, please use the "tutorial request" label in the issues tab to reach out to me:**


<h3>Guide</h3>

Actin is the most abundant protein in eukaryotic cells. As it is part of the cytoskeleton its function is essential for 
the maintenance of the cell's morphological structure. In neurons, it was only recently that researchers started paying 
attention to the peculiar subcellular organization and localization of actin. First focussing on the dendritic spines, 
later expanding to the axon.  

The axon initial segment (AIS) is defined as the most proximal 30-60 µm of the axon and is known for its sturdy 
actin-betaIV cytoskeletal structure which is known to facilitate the densely packed ion channels, regulatory and
scaffolding proteins on the membrane. The recent popularity of superresolution microscopy techniques like STORM and STED
has made the study of the localization of these proteins relatively easy and straightforward.

&nbsp;
<p align="center">
    <img src="static/Figure 1.svg" width="100%">
</p>
&nbsp;

Because of this property of the AIS many ion channels are localized either perpendicular to the actin rings
or attached to a scaffolding protein called Ankyrin G which is localized in between two actin rings. This results in ion 
channels like the Kv 1.1 (displayed below) appearing similar to superresolution images of actin.

&nbsp;
<div align="center">
    <img src="static/AIS.png" width="100%" style="mix-blend-mode: screen">
    <i align="center" style="font-size: 9px"> Example image of a rat hippocampal neuron AIS immunostained for Kv1.1.
Image made on a Zeiss AxioImager Z1 equipped with a STEDYCON scanhead detector for confocal and super-resolution imaging,
fitted with 4 APDs. Post-acquisition, image was deconvolved using Huygens Deconvolution Software  </i>
</div>

&nbsp;

This plugin was designed to detect and quantify the distance and the goodness of periodicity between cellular periodic structures. 
Additionally, it can be used to detect and quantify the periodicity shift between two periodic stuctures.

&nbsp;



<a href="static/WaveBreaker User Manual.pdf">
    <img src="static/UM BUT.svg" width="50%">  
</a>

<a href="static/TEMPLATE AUTOCORRELATION 0.17-0.21 (x10).xlsx">
    <img src="static/AC EX BUT.svg" width="50%">  
</a>

<a href="static/TEMPLATE CROSSCORRELATION (x15).xlsx">
    <img src="static/CC EX BUT.svg" width="50%">  
</a>

<a href="static/Post-processing.py">
    <img src="static/EX%20PY.svg" width="50%">
</a>


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

You can install `napari-k2-WaveBreaker` via [pip]:

    pip install napari-k2-WaveBreaker

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-k2-autocorrelation" is free and open source software

## Issues

If you encounter any problems, please file an issue along with a detailed description or reach out to me.

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
