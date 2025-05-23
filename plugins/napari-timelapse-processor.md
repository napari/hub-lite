
[![License BSD-3](https://img.shields.io/pypi/l/napari-timelapse-processor.svg?color=green)](https://github.com/jo-mueller/napari-timelapse-processor/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-timelapse-processor.svg?color=green)](https://pypi.org/project/napari-timelapse-processor)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-timelapse-processor.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-timelapse-processor/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-timelapse-processor/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-timelapse-processor/branch/main/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-timelapse-processor)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-timelapse-processor)](https://napari-hub.org/plugins/napari-timelapse-processor)

meta plugin to ease processing timelapse image data

## API

This plugin exposes two principal funcionalities:

### TimelapseConverter

The `TimelapseConverter` class allows you to stack or unstack any of the supported napari layers from 4D data into a list of 3D layers or vice versa. Currently supported layers are:

- `napari.layers.Image`
- `napari.layers.Labels`
- `napari.layers.Points`
- `napari.layers.Vectors`
- `napari.layers.Surface`

`napari.layers.Tracks` are intrinsically 4D and thus not supported.

**Unstacking example usage:**

```python
from napari_timelapse_processor import TimelapseConverter
import numpy as np

image_4d = np.random.rand(10, 32, 32, 32)  # 10 timepoints of 32x32x32 data
converter = TimelapseConverter()
list_of_images = converter.unstack(image_4d, layertype='napari.types.ImageData')
```

**Stacking example usage:**

```python
from napari_timelapse_processor import TimelapseConverter
import numpy as np

random_points = [np.random.rand(10, 3)  for _ in range(10)]  # 10 timepoints of 10 random 3D points
converter = TimelapseConverter()

# stack the points into a single 4D layer
stacked_points = converter.stack(random_points, layertype='napari.types.PointsData')
```

The `TimeLapseConverter` class also supports (un)stacking the `napari.layers.Layer` type (and its above-listed subclasses). Importantly, `features` that are associated with the respective layer are also (un)stacked.

**Layer example usage**

```python
from napari_timelapse_processor import TimelapseConverter
import numpy as np
from napari.layers import Points
import pandas as pd

random_points = [np.random.rand(10, 3)  for _ in range(10)]  # 10 timepoints of 10 random 3D points
random_features = [pd.DataFrame(np.random.rand(10)) for _ in range(10)]  # 10 timepoints of 10 random feature values

# create a list of 10 Points layers
points = [Points(random_points[i], properties=random_features[i]) for i in range(10)]

converter = TimelapseConverter()
stacked_points = converter.stack(points, layertype='napari.layers.Points')
```

## frame_by_frame

The frame-by-frame functionality provides a decorator that will inspect the decorated function for `TimelapseConverter`-compatible arguments and, if a 4D value is passed as argument, will automatically (un)stack the data before and after the function call. This allows for a more intuitive API when working with timelapse data. Currently supported type annotations are:

- `napari.types.ImageData`
- `napari.types.LabelsData`
- `napari.types.PointsData`
- `napari.types.VectorsData`
- `napari.types.SurfaceData`
- `napari.layers.Layer`
- `napari.layers.Image`
- `napari.layers.Labels`
- `napari.layers.Points`
- `napari.layers.Vectors`
- `napari.layers.Surface`

Additionally, the `frame_by_frame` supports parallelization with [dask.distributed](https://distributed.dask.org/en/latest/). To use it, simply pass the `use_dask=True` argument to the decorated function, even if the function itself does not require this argument. The decorater will then automatically parallelize the function call over the time-axis and remove the `use_dask` argument when calling the function.

**Example interactive code usage:** If you want to use the `frame_by_frame` functionality in, say, a Jupyter notebook, use it like this:

```python

from napari_timelapse_processor import frame_by_frame
import numpy as np

def my_function(image: 'napari.types.ImageData') -> 'napari.types.ImageData':
    return 2 * image

image_4d = np.random.rand(10, 32, 32, 32)  # 10 timepoints of 32x32x32 data

image_4d_processed = frame_by_frame(my_function)(image_4d)  # without dask
image_4d_processed = frame_by_frame(my_function)(image_4d, use_dask=True)  # with dask
```

**Example napari code** If you want to use the `frame_by_frame` functionality in a napari plugin, use it like this:

```python
from napari_timelapse_processor import frame_by_frame

@frame_by_frame
def my_function(image: 'napari.types.ImageData') -> 'napari.types.ImageData':
    return 2 * image
```

**Hint:** The `frame_by_frame` functionality runs under the assumption that input napari-data (e.g., an Image, a Surface, Points, etc) are *always* arguments and any other parameters are *always* keyword arguments. If this is not the case, the decorator will not work as intended.

```python

# This works
frame_by_frame(my_function)(image_4d, some_parameter=2, use_dask=True)

# This does not work
frame_by_frame(my_function)(image=image_4d, some_parameter=2, use_dask=True)
```

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-timelapse-processor` via [pip]:

    pip install napari-timelapse-processor




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-timelapse-processor" is free and open source software

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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
