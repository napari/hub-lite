
[![License MIT](https://img.shields.io/pypi/l/napari-turing.svg?color=green)](https://github.com/leoguignard/napari-turing/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-turing.svg?color=green)](https://pypi.org/project/napari-turing)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-turing.svg?color=green)](https://python.org)
[![tests](https://github.com/leoguignard/napari-turing/workflows/tests/badge.svg)](https://github.com/leoguignard/napari-turing/actions)
[![codecov](https://codecov.io/gh/leoguignard/napari-turing/branch/main/graph/badge.svg)](https://codecov.io/gh/leoguignard/napari-turing)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-turing)](https://napari-hub.org/plugins/napari-turing)

A plugin to run simple simulations of Turing patterns

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->
![example 1](img/turing_patterns.gif)
![example 2](img/turing_patterns2.gif)

## Installation

You can install `napari-turing` via [pip] after downloading the content of

    pip install napari-turing


To install latest version :

    pip install git+https://github.com/leoguignard/napari-turing.git

## Troubleshooting

If the installation does not work just with the previous command, it might be useful to first install [napari] for example that way:

    conda install napari

## Creating a new model

To create your own model, you can use the template for models [here](src/napari_turing/Models/ModelTemplate.py).

Note that a bit of knowledge in Python is probably necessary and it might not be completely trivial at first but you'll manage :)

First you need to name the concentrations that you will use with the following [line](src/napari_turing/Models/ModelTemplate.py#L40):
```python
    _concentration_names = ["A", "I"]
```

Then, you need to declare its variables. For example you can create a parameter named `mu_a` the following way ([here in the code](src/napari_turing/Models/ModelTemplate.py#L53-L60)):
```python
    mu_a = ModelParameter(
        name="mu_a",  # Name of the parameter
        description="Activator diffusion coefficient (10^-4)",  # Description of the parameter for napari
        value=2.8,  # Initial and default value
        min=1,  # Minimum value the parameter can take
        max=5,  # Maximum value the parameter can take
        exponent=1e-4,  # All values given to this instance of the class will but multiplied by this value
    )
```

Then you need to list the parameters that are necessary to run the model (usually all the paramaters declared previously) and the parameters that you will allow the user to tune (for example, sometimes some of the parameters are co-dependent and there is no point in being able to tune both of them). That should be done the following way ([here in the code](src/napari_turing/Models/ModelTemplate.py#L86-89)):
```python
    # These are the parameters that are necessary to run the equations.
    _necessary_parameters = [tau, k, mu_a, mu_i]
    # These are the parameters that can be modified via napari
    _tunable_parameters = _necessary_parameters
```

If you want, you can specify what the method will return as a string, it will be displayed in the napari viewer ([here in the code](src/napari_turing/Models/ModelTemplate.py#L90-L98)):
```python
    # This function allows to display some information about the model
    # in napari
    def __str__(self) -> str:
        return (
            "Equations (FitzHugh-Nagumo model):\n"
            "  Concentration of Activator (a) and Inhibitor (i)\n"
            "    - da/dt = mu_a * diffusion(a) + a - a^3 - i + k\n"
            "    - tau * di/dt = mu_i * diffusion(i) + a - i"
        )
```

Now that the basics are declared, you will need to declare how to initialize your concentrations the following way ([here in the code](src/napari_turing/Models/ModelTemplate.py#L100-L116)):
```python
    # The following allows to reset the values of the concentrations.
    # The function takes the name of the concentration to initialize.
    # If no name is given or if it is None all the concentrations are
    # reinitialized.
    #
    # The reason why this function is useful is that some models 
    # require specific initialisations for them to work correctly
    # In the following example the concentrations are reintinalized
    # to a random value between -1 and 1.
    # This is the default behavior, so if you don't need to change
    # it you don't have to implement the function.
    def init_concentrations(self, C: Optional[str] = None) -> None:
        if C is None:
            for ci in self.concentration_names():
                self[ci] = np.random.random((self.size, self.size)) * 2 - 1
        else:
            self[C] = np.random.random((self.size, self.size)) * 2 - 1
```
In the previous example, the all concentrations are initialized the same way. If you need to have different initializations, you can do it the following way for example ([from the GrayScott model](src/napari_turing/Models/GrayScott.py#L68-L76)):
```python
    def init_concentrations(self, C: Optional[str] = None) -> None:
        if C == "X" or C is None:
            self["X"] = np.ones((self.size, self.size))
        if C == "Y" or C is None:
            Y = np.zeros((self.size, self.size))
            nb_pos = 20
            pos = (np.random.random((2, nb_pos)) * self.size).astype(int)
            Y[pos[0], pos[1]] = 1
            self["Y"] = Y
```
In this model, there are two concentrations, `X` and `Y` which are initialized differenty. Note that they can be accessed using `self["X"]` or `self.X`.

Finally, you of course have to define the reaction equations and the diffusion equations. The way it is defined is with two functions, one for the reaction and one for the diffusion, that take as an input the name of the concentration to apply the function to and returns the new values. Then for each of your concentrations, their new values will be computed as followed:
```python
new_concentration = current_concentration + dt*(reaction + diffusion)
```

Here is an example for the reaction function ([here in the code](src/napari_turing/Models/ModelTemplate.py#L127-L136)):
```python 
    # This function defines the equations of the reactions.
    # It takes as an input which concentration to compute
    # (in this example we have to define how to compute A and I)
    def _reaction(self, c: str) -> np.ndarray:
        if c == "A":
            # Below is the reaction part of the equation (1)
            return self.A - self.A**3 - self.I + self.k 
        elif c == "I":
            # Below is the reaction part of the equation (2)
            return (self.A - self.I) / self.tau
```
Of course, if you have more concentrations, you will need to define more equations.

Here is an example for the reaction function ([here in the code](src/napari_turing/Models/ModelTemplate.py#L138-L166)):
```python
    # This function defines the equations of the diffusion.
    # It takes as an input which concentration to compute
    # (in this example we have to define how to compute A and I)
    # Here we compute the diffusion as follow:
    # A cell gives an equal fraction mu of its concentration to its neighbors
    # A cell recieves an equal fraction mu of concentration from its neighbors
    # Neighbors = (left, right, above, below)
    # In the case of oriented diffusion the amount recieved and given to the neighbors
    # is imbalanced according to the position of the neighbor.
    def _diffusion(self, c: str) -> np.ndarray:
        if c == "A":
            arr = self.A # Define the array of concentrations to diffuse for the reageant A
            mu = self.mu_a # Define the diffusion coefficient for the reageant A
        elif c == "I":
            arr = self.I # Define the array of concentrations to diffuse for the reageant I
            mu = self.mu_i # Define the diffusion coefficient for the reageant I
        
        # Computes what is recieved from neighboring cells
        from_cell = convolve(arr, self.kernel.value, mode="constant", cval=0)
        # Computes what is given to neighboring cells
        to_cell = self.nb_neighbs * arr

        # Computes the diffusion
        out = mu * (from_cell - to_cell) / (self.dx * self.dy)

        # In our case, the equation (2), for I specify that it has to be divided by tau
        if c == "I":
            out /= self.tau
        return out
```
The diffusion function is usually a standard one so it might not be necessary to overly change it.

You can find other model examples:
- [Brusselator](src/napari_turing/Models/Brusselator.py)
- [GrayScott](src/napari_turing/Models/GrayScott.py)
- [GameOfLife](src/napari_turing/Models/GameOfLife.py)

Once all that is done, let say you've saved your new model in the folder [Models](src/napari_turing/Models) under the name `NewModel.py` and the model class created is name `NewModel`. Then you need to declare you model in the [`_model_list.py`](src/napari_turing/Models/_model_list.py) file. To do so you need to add the following lines in the file:
```python
from enum import Enum
from .FitzHughNagumo import FitzHughNagumo
from .Brusselator import Brusselator
from .GrayScott import GrayScott
from .GameOfLife import GameOfLife
from .NewModel import NewModel ## THAT LINE HERE

class AvailableModels(Enum):
    FitzHughNagumo = FitzHughNagumo
    Brusselator = Brusselator
    GrayScott = GrayScott
    GameOfLife = GameOfLife
    NewModel = NewModel ## AND THAT OTHER LINE HERE
```

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [MIT] license,
"napari-turing" is free and open source software

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

[file an issue]: https://github.com/leoguignard/napari-turing/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
