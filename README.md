# Anacostia Warning System

Anacostia DC Air pollution and water warning system

## Getting Started

### Installing pipx

Install pipx using Homebrew on macOS:

```bash
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global
```

Install pipx via Scoop on Windows:

```bash
scoop install pipx
pipx ensurepath
```

### Installing Poetry

Install Poetry using pipx:

```bash
pipx install poetry
```

### Installing Dependencies

Lock dependencies and install them with Poetry:

```bash
poetry lock --no-update
poetry install
```

### Running the Application

Execute the application using Poetry:

```bash
poetry run python src/start.py
```

## Running Using Notebooks

In the `notebooks` directory, create `.ipynb` files that can utilize `requirements.txt` to install dependencies.