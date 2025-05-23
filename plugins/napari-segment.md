
[![License](https://img.shields.io/pypi/l/napari-segment.svg?color=green)](https://github.com/aaristov/napari-segment/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-segment.svg?color=green)](https://pypi.org/project/napari-segment)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-segment.svg?color=green)](https://python.org)
[![tests](https://github.com/aaristov/napari-segment/workflows/tests/badge.svg)](https://github.com/aaristov/napari-segment/actions)
[![codecov](https://codecov.io/gh/aaristov/napari-segment/branch/main/graph/badge.svg)](https://codecov.io/gh/aaristov/napari-segment)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-segment)](https://napari-hub.org/plugins/napari-segment)

Interactively segment organoids/spheroids/aggregates in brightfield/fluorescence from nd2 multipositional stack.
----------------------------------

![image](https://user-images.githubusercontent.com/11408456/201948817-255717a6-5f5c-45a2-ae01-2e0cbb1e29e8.png)


## Installation

```pip install napari-segment```

or

From napari plugin

![image](https://user-images.githubusercontent.com/11408456/201949692-33f94eaf-ac43-44dd-8c21-e9f9a460c5b2.png)


## Usage for segmentation

1. Drag your nd2 file into napari (otherwise try the Sample data from File / Open Sample / napari-segment)
2. Lauch Plugins -> napari-segment: Segment multipos
3. Select the brightfield channel
4. The data is lazily loaded from nd2 dataset and dynamically segmented in the viewer.
5. Binning 1-8 allows to skip small features and focus on bigger objects, also makes processing faster.
![image](https://user-images.githubusercontent.com/11408456/201701163-70c4af51-8a3a-42a0-adb9-32f0114eb49d.png)
6. Various preprocessing modes allow segmentation of different objects:
![image](https://user-images.githubusercontent.com/11408456/201701809-f16a23ea-d14a-4b38-8b8c-08a113416509.png)

  - Invert: will use the dark shadow around aggregate - best for very old aggregates , out of focus (File / Open Sample / napari-segment / Old aggregate)
  
  ![image](https://user-images.githubusercontent.com/11408456/201701950-efd86fae-d85b-471c-bb44-a0e328e26adc.png)

  - Gradient: best for very sharp edges, early aggregates, single cells (File / Open Sample / napari-segment / Early aggregate) 
  
  ![image](https://user-images.githubusercontent.com/11408456/201705697-5d0d0643-44b6-4cb9-9208-4a29dd899d8c.png)
  
  
  - Gauss diff: Fluorescence images
  The result of preprocessing will be shown in the "Preprocessing" layer.
7. Smooth, Theshold and Erode parameters allow you to adjust the preliminary segmentation -> they all will appear in the "Detections" layer as outlines 

  ![image](https://user-images.githubusercontent.com/11408456/201703675-cff6bac1-bb2a-4d45-963f-6e6d00309c77.png)

8. Min/max diameter and eccentricity allow you to filter out unwanted regions -> the good regions will appear in the "selected labels" layer as filled areas.

![image](https://user-images.githubusercontent.com/11408456/201703754-2c83a8d6-70c2-444a-8e30-54a39c901cd0.png)
![image](https://user-images.githubusercontent.com/11408456/201707025-9121f0dc-3939-48f0-ae75-884891be8d66.png)


9. Once satisfied, click "Save the params!" - it will automatically create file.nd2.params.yml file, so you can recall how the segmentation was done. Next time you open the same dataset, the parameters will be loaded automatically from this file. 

10. Next section is for quantifying the sizes. Pixel size will be retrieved automatically from metadata. If not: update it manually and click Update plots to see the correct sizes. Click on any suspected value to see the corresponding frame and try to adjust the above parameters. 

![image](https://user-images.githubusercontent.com/11408456/201704881-b2303b9a-50c6-49c7-80ff-a6099cc2a151.png)

11. If impossible to get good results with automatic pipeline, click Clone for manual correction: this will create an editable "Manual" layer which you can edin with built-in tools in napari. Click "Update plots" to see the updated values. 

12. "Save csv!" will generate a csv file with regionprops. 


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-segment" is free and open source software

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

[file an issue]: https://github.com/aaristov/napari-segment/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
