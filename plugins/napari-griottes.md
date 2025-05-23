
[![License](https://img.shields.io/pypi/l/napari-griottes.svg?color=green)](https://github.com/BaroudLab/napari-griottes/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-griottes.svg?color=green)](https://pypi.org/project/napari-griottes)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-griottes.svg?color=green)](https://python.org)
[![tests](https://github.com/BaroudLab/napari-griottes/workflows/tests/badge.svg)](https://github.com/BaroudLab/napari-griottes/actions)
[![codecov](https://codecov.io/gh/BaroudLab/napari-griottes/branch/main/graph/badge.svg)](https://codecov.io/gh/BaroudLab/napari-griottes)

[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-griottes)](https://napari-hub.org/plugins/napari-griottes)



Use [🍒  `Griottes` 🍒](https://github.com/BaroudLab/Griottes) in napari!

----------------------------------



https://user-images.githubusercontent.com/11408456/224119160-c381091d-8275-449e-9cf4-679ab474acd2.mp4




## Installation

Install from napari

![image](https://user-images.githubusercontent.com/11408456/224108834-f484ba37-50f4-415e-bdfb-509c6c5b88c4.png)


You can install `napari-griottes` via [pip]:

    pip install napari-griottes



To install latest development version :

    pip install git+https://github.com/BaroudLab/napari-griottes.git



## Usage

### Starting with labels:

1. Open the plugin in Plugins/napari-griottes
2. Make sure the layer with labels is selected
3. Click Run once to get centers
4. Click Run second time to get graph
5. Select the right kind of graph in the drop-down menu
6. Adjust the distance
7. Adjust thickness

![Screenshot from three labels geometric contact mp4](https://user-images.githubusercontent.com/11408456/167371516-05db2ba5-cdfc-47c4-a488-8f46afd0ae5b.png)



https://user-images.githubusercontent.com/11408456/167825581-47c39884-34cf-4b5c-ad84-a4572217559d.mp4



### Starting with Segmented cells

1. Open sample data: File / Open Sample / napari-griottes / Zebrafish 2D with labels
2. Select the top layer and covert it to labels (right click - Convert to labels)
3. Run the plugin once to get the centers of labels
4. Run the plugin twice to get the connections
5. Proceed with graph creation


![Screenshot from cells graphs mp4](https://user-images.githubusercontent.com/11408456/167372895-3c9036b9-af50-4575-bcf3-1805eb261bd7.png)




https://user-images.githubusercontent.com/11408456/168237170-b43afd5a-26a4-4cdc-bc42-d3f46f138536.mp4


### Saving and recovering the graph

Any graph you see in napari can be saved in .json format.
1. Select he layers with connections
2. Click File/Save Selected Layer
3. Choose Griottes in drop-down menu
4. Save

In order to recover a previously saved graph in napari, you can simply drag-n-drop your file into napari, or use file open fialog.



https://user-images.githubusercontent.com/11408456/167845853-e7071199-3f58-4d11-8d7b-c1358a150e6b.mp4


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-griottes" is free and open source software

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

[file an issue]: https://github.com/BaroudLab/napari-griottes/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
