# anacostia-warning-system
Anacostia DC Air pollution and water warning system


## Getting Started

### Installing pipx
https://pipx.pypa.io/stable/installation/

#### On macOS:

```
brew install pipx

pipx ensurepath

sudo pipx ensurepath --global
```

optional to allow pipx actions in global scope. See "Global installation" section below.


#### On Windows:
Install via Scoop:

```
scoop install pipx

pipx ensurepath
```

### Installing poetry
```pipx install poetry```

### Installing Dependencies

```
poetry lock --no-update

poetry install
```

### Running application
```
poetry run python src/start.py
```