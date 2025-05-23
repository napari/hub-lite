
[![License](https://img.shields.io/pypi/l/napari-console.svg?color=green)](https://github.com/napari/napari-console/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-console.svg?color=green)](https://pypi.org/project/napari-console)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-console.svg?color=green)](https://python.org)
[![tests](https://github.com/napari/napari-console/workflows/tests/badge.svg)](https://github.com/napari/napari-console/actions)
[![codecov](https://codecov.io/gh/napari/napari-console/branch/main/graph/badge.svg)](https://codecov.io/gh/napari/napari-console)

A plugin that adds a console to napari

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Local variables

In napari-console 0.0.8 and earlier, the console `locals()` namespace only
contained a reference to the napari viewer that enclosed the console.

Since version 0.0.9, it instead contains everything in the enclosing frame that
called napari. That is, if your Python code is:

```python
import napari
import numpy as np
from scipy import ndimage as ndi

image = np.random.random((500, 500))
labels = ndi.label(image > 0.7)[0]

viewer, image_layer = napari.imshow(image)
labels_layer = viewer.add_labels(labels)

napari.run()
```

Then the napari console will have the variables `np`, `napari`, `ndi`, `image`,
`labels`, `viewer`, `image_layer`, and `labels_layer` in its namespace.

This is implemented by inspecting the Python stack when the console is first
instantiated, finding the first frame that is outside of the `napari_console`,
`napari`, and `in_n_out` modules, and passing the variables in the frame's
`f_locals` and `f_globals` to the console namespace.

If you want to disable this behavior (for example, because you are embedding
napari and the console within some larger application), you can add
`NAPARI_EMBED=1` to your environment variables before instantiating the
console.

## Installation

You can install `napari-console` via [pip]:

    pip install napari-console

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-console" is free and open source software

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
[file an issue]: https://github.com/sofroniewn/napari-console/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
