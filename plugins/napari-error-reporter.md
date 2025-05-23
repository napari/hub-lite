
[![License](https://img.shields.io/pypi/l/napari-error-reporter.svg?color=green)](https://github.com/tlambert03/napari-error-reporter/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-error-reporter.svg?color=green)](https://pypi.org/project/napari-error-reporter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-error-reporter.svg?color=green)](https://python.org)
[![CI](https://github.com/tlambert03/napari-error-reporter/actions/workflows/ci.yml/badge.svg)](https://github.com/tlambert03/napari-error-reporter/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/tlambert03/napari-error-reporter/branch/main/graph/badge.svg)](https://codecov.io/gh/tlambert03/napari-error-reporter)

Want to help out napari?  Install this plugin!

This plugin will automatically send error reports to napari (via
[sentry.io](https://sentry.io)) whenever an exception occurs while you are using
napari.

The first time you run napari after installing this plugin an opt-in
notification will appear (Be sure to click "yes", otherwise no reports will be
collected or sent).  You may opt back out at any time in napari's help menu.

Every effort is made to strip these reports of personally identifiable
information.  Here is an example exception event:

<details>

<summary>Example bug report</summary>

```python
{
    'breadcrumbs': {
        'values': [
            {
                'category': 'subprocess',
                'data': {},
                'message': 'sw_vers -productVersion',
                'timestamp': '2022-02-02T01:30:00.216738Z',
                'type': 'subprocess'
            }
        ]
    },
    'contexts': {
        'runtime': {
            'build': '3.9.9 | packaged by conda-forge | (main, Dec 20 2021, 02:41:37) \n[Clang 11.1.0 ]',
            'name': 'CPython',
            'version': '3.9.9'
        }
    },
    'environment': 'macOS-10.15.7-x86_64-i386-64bit',
    'event_id': '02dd8ddd3a4b4743af3d7d7a09949df4',
    'exception': {
        'values': [
            {
                'mechanism': None,
                'module': None,
                'stacktrace': {
                    'frames': [
                        {
                            'context_line': '                x = 1 / 0',
                            'filename': 'napari_error_reporter/_util.py',
                            'function': 'get_sample_event',
                            'in_app': True,
                            'lineno': 130,
                            'module': 'napari_error_reporter._util',
                            'post_context': [
                                '            except Exception:',
                                '                with sentry_sdk.push_scope() as scope:',
                                '                    for k, v in _get_tags().items():',
                                '                        scope.set_tag(k, v)',
                                '                    del v, k, scope'
                            ],
                            'pre_context': [
                                "            # remove locals that wouldn't really be there",
                                '            del settings, _trans, kwargs, client, EVENT',
                                '            try:',
                                '                some_variable = 1',
                                '                another_variable = "my_string"'
                            ]
                        }
                    ]
                },
                'type': 'ZeroDivisionError',
                'value': 'division by zero'
            }
        ]
    },
    'extra': {'sys.argv': ['napari']},
    'level': 'error',
    'modules': {
        'aicsimageio': '4.5.2',
        'aicspylibczi': '3.0.4',
        'aiohttp': '3.8.1',
        'aiosignal': '1.2.0',
        'alabaster': '0.7.12',
        'anyio': '3.5.0',
        'appdirs': '1.4.4',
        'appnope': '0.1.2',
        'argon2-cffi': '21.3.0',
        'argon2-cffi-bindings': '21.2.0',
        'arrow': '1.2.1',
        'asciitree': '0.3.3',
        'asttokens': '2.0.5',
        'async-timeout': '4.0.2',
        'atomium': '1.0.11',
        'attrs': '21.4.0',
        'autopep8': '1.6.0',
        'babel': '2.9.1',
        'backcall': '0.2.0',
        'bcrypt': '3.2.0',
        'beautifulsoup4': '4.10.0',
        'binaryornot': '0.4.4',
        'black': '20.8b1',
        'bleach': '4.1.0',
        'bracex': '2.2.1',
        'build': '0.7.0',
        'cachey': '0.2.1',
        'cellpose': '0.6.5',
        'certifi': '2021.10.8',
        'cffi': '1.15.0',
        'cfgv': '3.3.1',
        'chardet': '4.0.0',
        'charset-normalizer': '2.0.10',
        'check-manifest': '0.47',
        'click': '7.1.2',
        'click-option-group': '0.5.3',
        'cloudpickle': '2.0.0',
        'colorama': '0.4.4',
        'commonmark': '0.9.1',
        'cookiecutter': '1.7.3',
        'coverage': '6.2',
        'cryptography': '36.0.1',
        'cycler': '0.11.0',
        'dask': '2022.1.0',
        'debugpy': '1.5.1',
        'decorator': '5.1.1',
        'defusedxml': '0.7.1',
        'distlib': '0.3.4',
        'dnspython': '2.2.0',
        'docstring-parser': '0.13',
        'docutils': '0.16',
        'elementpath': '2.4.0',
        'email-validator': '1.1.3',
        'entrypoints': '0.3',
        'executing': '0.8.2',
        'fancycompleter': '0.9.1',
        'fasteners': '0.17.2',
        'fastremap': '1.12.2',
        'filelock': '3.4.2',
        'flake8': '3.8.4',
        'fonttools': '4.28.5',
        'freetype-py': '2.2.0',
        'frozenlist': '1.3.0',
        'fsspec': '2022.1.0',
        'furo': '2022.1.2',
        'gitdb': '4.0.9',
        'gitpython': '3.1.26',
        'greenlet': '1.1.2',
        'heapdict': '1.0.1',
        'hsluv': '5.0.2',
        'hypothesis': '6.35.1',
        'identify': '2.4.4',
        'idna': '3.3',
        'imagecodecs': '2021.11.20',
        'imageio': '2.10.5',
        'imageio-ffmpeg': '0.4.5',
        'imagesize': '1.3.0',
        'importlib-metadata': '4.10.1',
        'iniconfig': '1.1.1',
        'install': '1.3.5',
        'intervaltree': '3.1.0',
        'ipykernel': '6.7.0',
        'ipython': '8.0.0',
        'ipython-genutils': '0.2.0',
        'ipywidgets': '7.6.5',
        'jedi': '0.18.1',
        'jinja2': '3.0.3',
        'jinja2-time': '0.2.0',
        'jsonschema': '3.2.0',
        'jupyter': '1.0.0',
        'jupyter-book': '0.12.1',
        'jupyter-cache': '0.4.3',
        'jupyter-client': '7.1.1',
        'jupyter-console': '6.4.0',
        'jupyter-core': '4.9.1',
        'jupyter-server': '1.13.3',
        'jupyter-server-mathjax': '0.2.3',
        'jupyter-sphinx': '0.3.2',
        'jupyterlab-pygments': '0.1.2',
        'jupyterlab-widgets': '1.0.2',
        'jupytext': '1.11.5',
        'kiwisolver': '1.3.2',
        'latexcodec': '2.0.1',
        'linkify-it-py': '1.0.3',
        'llvmlite': '0.38.0',
        'locket': '0.2.1',
        'loguru': '0.5.3',
        'lxml': '4.7.1',
        'magicgui': '0.3.5.dev18+g78d1687',
        'markdown-it-py': '1.1.0',
        'markupsafe': '2.0.1',
        'matplotlib': '3.5.1',
        'matplotlib-inline': '0.1.3',
        'mccabe': '0.6.1',
        'mdit-py-plugins': '0.2.8',
        'meshzoo': '0.9.2',
        'mistune': '0.8.4',
        'mrc': '0.2.0',
        'msgpack': '1.0.3',
        'multidict': '5.2.0',
        'mypy': '0.931',
        'mypy-extensions': '0.4.3',
        'myst-nb': '0.13.1',
        'myst-parser': '0.15.2',
        'napari': '0.4.14rc1.dev4+gcdf58d44b',
        'napari-aicsimageio': '0.4.1',
        'napari-console': '0.0.4',
        'napari-dv': '0.2.7.dev0+g54e1691.d20220128',
        'napari-error-reporter': '0.1.dev1+g1b388f2.d20220201',
        'napari-hello': '0.0.1',
        'napari-math': '0.0.1a0',
        'napari-micromanager': '0.0.1rc6.dev14+g5149788.d20220128',
        'napari-molecule-reader': '0.1.2.dev1+gc2ec2de',
        'napari-plugin-engine': '0.2.0',
        'napari-pyclesperanto-assistant': '0.12.0',
        'napari-skimage-regionprops': '0.2.9',
        'napari-svg': '0.1.6',
        'napari-time-slicer': '0.4.2',
        'napari-workflows': '0.1.2',
        'natsort': '8.0.2',
        'nbclient': '0.5.10',
        'nbconvert': '6.4.0',
        'nbdime': '3.1.1',
        'nbformat': '5.1.3',
        'nd2': '0.1.4',
        'nest-asyncio': '1.5.4',
        'networkx': '2.6.3',
        'nodeenv': '1.6.0',
        'notebook': '6.4.7',
        'npe2': '0.1.1',
        'numba': '0.55.0',
        'numcodecs': '0.9.1',
        'numpy': '1.20.3',
        'numpydoc': '1.1.0',
        'ome-types': '0.2.10',
        'opencv-python-headless': '4.5.5.62',
        'packaging': '21.3',
        'pandas': '1.3.5',
        'pandocfilters': '1.5.0',
        'paramiko': '2.9.2',
        'parso': '0.8.3',
        'partd': '1.2.0',
        'pathspec': '0.9.0',
        'pdbpp': '0.10.3',
        'peewee': '3.14.8',
        'pep517': '0.12.0',
        'pexpect': '4.8.0',
        'pickleshare': '0.7.5',
        'pillow': '8.4.0',
        'pint': '0.18',
        'pip': '21.3.1',
        'platformdirs': '2.4.1',
        'pluggy': '1.0.0',
        'pooch': '1.5.2',
        'poyo': '0.5.0',
        'pre-commit': '2.16.0',
        'prometheus-client': '0.12.0',
        'prompt-toolkit': '3.0.24',
        'psutil': '5.9.0',
        'psygnal': '0.2.0',
        'ptyprocess': '0.7.0',
        'pure-eval': '0.2.1',
        'py': '1.11.0',
        'pybtex': '0.24.0',
        'pybtex-docutils': '1.0.1',
        'pyclesperanto-prototype': '0.12.0',
        'pycodestyle': '2.8.0',
        'pycparser': '2.21',
        'pydantic': '1.9.0',
        'pydata-sphinx-theme': '0.7.2',
        'pyflakes': '2.2.0',
        'pygments': '2.11.2',
        'pymmcore': '10.1.1.70.5',
        'pymmcore-plus': '0.1.8',
        'pynacl': '1.5.0',
        'pyopencl': '2021.2.13',
        'pyopengl': '3.1.5',
        'pyparsing': '3.0.6',
        'pyperclip': '1.8.2',
        'pyrepl': '0.9.0',
        'pyro5': '5.13.1',
        'pyrsistent': '0.18.1',
        'pyside2': '5.15.2.1',
        'pytest': '6.2.5',
        'pytest-cookies': '0.6.1',
        'pytest-cov': '3.0.0',
        'pytest-faulthandler': '2.0.1',
        'pytest-order': '1.0.1',
        'pytest-qt': '4.0.2',
        'python-dateutil': '2.8.2',
        'python-dotenv': '0.19.2',
        'python-slugify': '5.0.2',
        'pytomlpp': '1.0.10',
        'pytools': '2021.2.9',
        'pytz': '2021.3',
        'pywavelets': '1.2.0',
        'pyyaml': '6.0',
        'pyzmq': '22.3.0',
        'qtconsole': '5.2.2',
        'qtpy': '2.0.0',
        'regex': '2021.11.10',
        'requests': '2.27.1',
        'rich': '11.0.0',
        'rmsd': '1.4',
        'ruamel.yaml': '0.17.20',
        'ruamel.yaml.clib': '0.2.6',
        'scikit-image': '0.19.1',
        'scipy': '1.7.3',
        'semgrep': '0.78.0',
        'send2trash': '1.8.0',
        'sentry-sdk': '1.5.4',
        'serpent': '1.40',
        'setuptools': '60.5.0',
        'shiboken2': '5.15.2.1',
        'six': '1.16.0',
        'smmap': '5.0.0',
        'sniffio': '1.2.0',
        'snowballstemmer': '2.2.0',
        'sortedcontainers': '2.4.0',
        'soupsieve': '2.3.1',
        'sourcery-cli': '0.10.0',
        'sphinx': '4.4.0',
        'sphinx-autodoc-typehints': '1.12.0',
        'sphinx-book-theme': '0.1.10',
        'sphinx-comments': '0.0.3',
        'sphinx-copybutton': '0.4.0',
        'sphinx-external-toc': '0.2.3',
        'sphinx-jupyterbook-latex': '0.4.6',
        'sphinx-multitoc-numbering': '0.1.3',
        'sphinx-panels': '0.6.0',
        'sphinx-tabs': '3.2.0',
        'sphinx-thebe': '0.0.10',
        'sphinx-togglebutton': '0.2.3',
        'sphinxcontrib-applehelp': '1.0.2',
        'sphinxcontrib-bibtex': '2.2.1',
        'sphinxcontrib-devhelp': '1.0.2',
        'sphinxcontrib-htmlhelp': '2.0.0',
        'sphinxcontrib-jsmath': '1.0.1',
        'sphinxcontrib-qthelp': '1.0.3',
        'sphinxcontrib-serializinghtml': '1.1.5',
        'sqlalchemy': '1.4.29',
        'stack-data': '0.1.4',
        'superqt': '0.2.5.post2.dev7+ga49bcd7',
        'tensorstore': '0.1.16',
        'terminado': '0.12.1',
        'testpath': '0.5.0',
        'text-unidecode': '1.3',
        'tifffile': '2021.11.2',
        'toml': '0.10.2',
        'tomli': '2.0.0',
        'toolz': '0.11.2',
        'torch': '1.10.1',
        'tornado': '6.1',
        'tox': '3.24.5',
        'tox-conda': '0.9.1',
        'tqdm': '4.62.3',
        'traitlets': '5.1.1',
        'transforms3d': '0.3.1',
        'transitions': '0.8.10',
        'typed-ast': '1.5.1',
        'typer': '0.4.0',
        'typing-extensions': '4.0.1',
        'uc-micro-py': '1.0.1',
        'urllib3': '1.26.8',
        'useq-schema': '0.1.1.dev13+g01d1b46.d20220120',
        'valerius': '0.2.0',
        'virtualenv': '20.13.0',
        'vispy': '0.9.4',
        'watchdog': '2.1.6',
        'wcmatch': '8.3',
        'wcwidth': '0.2.5',
        'webencodings': '0.5.1',
        'websocket-client': '1.2.3',
        'wheel': '0.37.1',
        'widgetsnbextension': '3.5.2',
        'wmctrl': '0.4',
        'wrapt': '1.13.3',
        'wurlitzer': '3.0.2',
        'xarray': '0.20.2',
        'xmlschema': '1.9.2',
        'yarl': '1.7.2',
        'zarr': '2.10.3',
        'zipp': '3.7.0'
    },
    'platform': 'python',
    'release': '0.4.14rc1.dev4+gcdf58d44b',
    'sdk': {
        'integrations': [
            'aiohttp',
            'argv',
            'atexit',
            'dedupe',
            'excepthook',
            'logging',
            'modules',
            'sqlalchemy',
            'stdlib',
            'threading',
            'tornado'
        ],
        'name': 'sentry.python',
        'packages': [{'name': 'pypi:sentry-sdk', 'version': '1.5.4'}],
        'version': '1.5.4'
    },
    'server_name': '',
    'tags': {
        'platform.name': 'MacOS 10.15.7',
        'platform.system': 'Darwin',
        'qtpy.API_NAME': 'PySide2',
        'qtpy.QT_VERSION': '5.15.2'
    },
    'timestamp': '2022-02-02T01:30:00.229122Z'
}
```

</details>

> ***NOTE**: in the opt-in dialog, there is a checkbox labeled "include local variables",
checking this will include the value of variables in the local scope when an exception
occurs.  While these can be very useful when interpreting a bug report, they may
occasionally include local file path strings.  If that concerns you, please leave this
box unchecked*

## Install

This plugin requires napari version 0.4.15 or greater, or the `main` branch with PR
[napari/napari#4055](https://github.com/napari/napari/pull/4055).

Install via pip with:

```sh
pip install napari-error-reporter
```

or in the built-in plugin installer (a restart will be required):

<img width="503" alt="Untitled" src="https://user-images.githubusercontent.com/1609449/153915128-09a5e3d7-8561-4c17-b543-5ea172e3e860.png">


Thank you!!

## Privacy FAQ

Even with the multiple layers of opt-ins, and the attempts to wipe all personal info
prior to sending reports, we understand that privacy is always a concern.

### Do you collect personal info?

We make every attempt to collect ***no*** personally identifiable information.  No
name, location, IP address, etc...  We do collect your
([`uuid.getnode()`](https://docs.python.org/3.10/library/uuid.html#uuid.getnode)) to
be able to track bug resolution over time. As mentioned above, allowing local
variables to be collected may occasionally include a file path in the log.
If that concerns you, please leave that unchecked.

### Is this shipped with napari?

`napari-error-reporter` is **not** bundled with napari or listed as a napari dependency.
In order for reports to be sent, you must first install this plugin yourself, and then
opt in on the next launch.  If you uninstall the plugin, no more reports can be sent.

### Who can access these reports?

Only the following napari core developers have access to these reports.
If [this](https://raw.githubusercontent.com/tlambert03/napari-error-reporter/main/ADMINS)
list changes in the future, you will be asked to opt-in again in napari:

- Juan Nunez-Iglesias ([@jni](https://github.com/jni))
- Talley Lambert ([@tlambert03](https://github.com/tlambert03))

*This plugin is **not** associated with the Chan Zuckerberg Initiative*.

### How will these reports be used?

Commonly occuring errors will be will be manually purged of file paths and
local variables and posted to https://github.com/napari/napari/issues

### How long is data retained

Sentry retains event data for 90 days by default.  For complete details,
see Sentry's page on [Security & Compliance](https://sentry.io/security/)
