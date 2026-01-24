# Welcome to EDA_simplifier

|  |  |
|------------------------------------|------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/eda_simplifier.svg)](https://pypi.org/project/eda_simplifier/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/eda_simplifier.svg)](https://pypi.org/project/eda_simplifier/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) [![build](https://github.com/UBC-MDS/eda_simplifier/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/eda_simplifier/actions/workflows/build.yml) [![deploy](https://github.com/UBC-MDS/eda_simplifier/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/eda_simplifier/actions/workflows/deploy.yml) |

*TODO: the above badges that indicate python version and package version
will only work if your package is on PyPI. If you don't plan to publish
to PyPI, you can remove them.*

## Package Summary

EDA_simplifier is a project that streamlines exploratory data analysis
(EDA) for any pandas DataFrame. This package provides functions that
consolidate many repetitive steps in EDA, serving as a first pass to
quickly gain a holistic view of a dataset. Within the larger Python
ecosystem, it requires Pandas and primarily builds upon Altair. While
Altair is powerful, it can also be verbose and syntactically
restrictive. As a result, many functions in this project act as wrappers
around Altair, providing sensible defaults and abstractions to simplify
the EDA process. Although automated EDA reporting libraries exist, most
focus on large-scale HTML reports or one-liner summaries. Therefore the
EDA simplifier package provides a intermediate between raw Altair-based
EDA plotting and full-automated report libraries.

## Functions

- `dataset_overview`:
    Generates a consolidated exploratory summary of a dataset by
    combining key information typically obtained from multiple pandas
    methods such as `.info()`, `.describe()`, and `.shape`. The function
    returns the dataset dimensions, column data types, missing value
    counts, and summary statistics in a single simplified structure to
    streamline the initial exploratory data analysis process.

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

- `all_distributions`:
    The main interface for column-level EDA distribution visualizations
    for numeric and categorical columns. Automatically identifies each
    columns data types and routes them to the appropriate plotting
    functions (`numeric` and `categorical_plot`). Also includes a
    manual overrides for ambiguous columns via explicit user input where
    the default columns data types may be incorrectly represented
    (using the hidden `_ambiguous_columns_split` function).

- `_ambiguous_columns_split`:
    Separates numeric and categorical columns for a pandas Dataframe,
    and applies overrides for ambiguous cases via input. Hidden function used purely for
    all_distributions function.

## Get started

You can install this package into your preferred Python environment:

``` bash
# create a new empty conda environment with Python 3.11 (and pip by proxy):
conda create -n eda_simplifier python=3.11 
# activate the new environment
conda activate eda_simplifier 
```

To verify the package passes all the unit tests:

``` bash
# To install and use package (in edit mode with dev dependencies):
pip install -e ".[dev]"  
# Run unit tests:
pytest -v

# Deactivate the conda environment when done:
conda deactivate
```

TODO: Add a brief example of how to use the package to this section

To use eda_simplifier in your code:

``` python
>>> import pandas as pd
>>> from eda_simplifier.simplify import dataset_overview

>>> df = pd.DataFrame({
    "artist": ["A", "B", "C"],
    "popularity": [80, 75, None],
    "danceability": [0.8, 0.6, 0.9]
})

>>> summary = dataset_overview(df)
```

## Contributors

- Diana Cornescu
- Johnson Chuang
- Lavanya Gupta
- Tiantong Yin

## Copyright

- Copyright © Diana Cornescu, Johnson Chuang, Lavanya Gupta & Tiantong
    Yin.
- Free software distributed under the [MIT License](./LICENSE).
