# Welcome to EDA_simplifier

[![Deploy](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/ci.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/ci.yml)

[![Deploy](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/cd.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/cd.yml)

[![Deploy](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/docs-publish.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group38_EDAsimplifier/actions/workflows/docs-publish.yml)

[![codecov](https://codecov.io/github/UBC-MDS/DSCI_524_Group38_EDAsimplifier/graph/badge.svg?token=1ZTk0JhKhM)](https://codecov.io/github/UBC-MDS/DSCI_524_Group38_EDAsimplifier)

## Package Summary

EDA_simplifier is a project that streamlines exploratory data analysis
(EDA) for any pandas DataFrame. This package provides functions that
consolidate many repetitive steps in EDA, serving as a first pass to
quickly gain a holistic view of a dataset. Specifically, it acts as an Altair
wrapper that takes in a Pandas DataFrame and has the following functions: 

### Functions

- `dataset_overview`:
    Generates a consolidated exploratory summary of a dataset by
    combining key information typically obtained from multiple pandas
    methods such as `.info()`, `.describe()`, and `.shape`. The function
    returns the dataset dimensions, column data types, missing value
    counts, and summary statistics in a single simplified structure to
    streamline the initial exploratory data analysis process.

- `all_distributions`:
    The main interface for column-level EDA distribution visualizations
    for numeric and categorical columns. Automatically identifies each
    columns data types and routes them to the appropriate plotting
    functions (`numeric` and `categorical_plot`). Also includes a
    manual overrides for ambiguous columns via explicit user input where
    the default columns data types may be incorrectly represented
    (using the hidden `_ambiguous_columns_split` function).

- `numeric`:
    Perform exploratory data analysis
    (EDA) on numerical features in a dataset. Generates visualizations
    for specified numerical columns to help with initial exploratory
    analysis. It produces histogram plots to examine distributions,
    correlation plots to identify relationships between features,
    missing values, and other relevant numerical summaries.

- `categorical_plot`:
    Creates Altair plots for the specified categorical columns. Creates
    bar charts and pie charts for each features. Also create box plots
    or stacked bar charts for each feature against the target depending
    on if the target is categorical or numerical.

# Installation

## User Installation

You can install this package from [TestPyPI](https://test.pypi.org/project/eda_simplifier/) into your preferred Python environment:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ eda_simplifier
```

## Developer Installation

For contribution guidelines and recommended workflow, see [CONTRIBUTING.md](CONTRIBUTING.md).

First, clone the repository from GitHub and navigate into the project directory:

```bash
git clone git@github.com:UBC-MDS/DSCI_524_Group38_EDAsimplifier.git
cd DSCI_524_Group38_EDAsimplifier/
```

Set up your development environment using one of the following methods:

<details>
<summary><b>Method 1: Using conda with environment.yml (recommended)</b></summary>
Create a conda environment and install the package:

```bash
conda env create -f environment.yml #after cd into cloned repo
conda activate eda_simplifier
pip install -e ".[dev,tests,docs]"
#depends on the scope - can do just ".[dev]" for a more minimalistic version.
```
</details>

<details>
<summary><b>Method 2: Using pip only</b></summary>
Install directly into the current Python environment:

```bash
pip install -e ".[dev,tests,docs]"
#depends on the scope - can do just ".[dev]" for a more minimalistic version.
```
</details>

Once the package is installed, you will see a message like:

```bash
Successfully installed eda_simplifier-xx.xx.xx
```

After a completed install, the following can be checked:

<details>
<summary><b>Unit Test</b></summary>
```bash
pytest -v
```
</details>


<details>
<summary><b>Linting and Formatting Checks</b></summary>
    
```bash
# Linting
ruff check .

# Format check
black --check .
```
</details>

<details>
<summary><b>Building and Rendering Documentation</b></summary>

```bash
quartodoc build
quarto render
```
</details>

To deactivate the conda environment (if you used Method 1):

```bash
conda deactivate
```

### Deployment (CI/CD Workflows)

Our documentation and package deployment are automated with GitHub Actions:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `build.yml` | PR and push to main | Lint and test |
| `deploy.yml` | Push to main | Publish to [TestPyPI](https://test.pypi.org/project/eda_simplifier/) |
| `docs-publish.yml` | Push to main | Build, render, and publish docs to GitHub Pages |


# Getting Started & Demo Example:

## Usage
The full [API reference](https://ubc-mds.github.io/DSCI_524_Group38_EDAsimplifier/reference/) can be referenced for more information and examples for each function.

To use eda_simplifier in your code:

``` python
import pandas as pd
from eda_simplifier.simplify import dataset_overview

df = pd.DataFrame({
    "artist": ["A", "B", "C"],
    "popularity": [80, 75, None],
    "danceability": [0.8, 0.6, 0.9]
    })

summary = dataset_overview(df)
```

## Python Ecosystem
Within the larger Python ecosystem, it requires Pandas and primarily builds upon Altair. While
Altair is powerful, it can also be verbose and syntactically restrictive. As a result, many functions in this project act as wrappers
around Altair, providing sensible defaults and abstractions to simplify
the EDA process. Although automated EDA reporting libraries exist, most
focus on large-scale HTML reports or one-liner summaries. Therefore the
EDA simplifier package provides a intermediate between raw Altair-based
EDA plotting and full-automated report libraries.

## Contributors

- Diana Cornescu
- Johnson Chuang
- Lavanya Gupta
- Tiantong Yin

## Copyright

- Copyright © Diana Cornescu, Johnson Chuang, Lavanya Gupta & Tiantong
    Yin.
- Free software distributed under the [MIT License](./LICENSE).
