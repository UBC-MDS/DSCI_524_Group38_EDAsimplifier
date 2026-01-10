---
editor_options: 
  markdown: 
    wrap: 72
---

# Welcome to EDA_simplifier

|  |  |
|------------------------------------|------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/eda_simplifier.svg)](https://pypi.org/project/eda_simplifier/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/eda_simplifier.svg)](https://pypi.org/project/eda_simplifier/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

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

-   `dataset_overview(df)`:\
    Generates a consolidated exploratory summary of a dataset by
    combining key information typically obtained from multiple pandas
    methods such as `.info()`, `.describe()`, and `.shape`. The function
    returns the dataset dimensions, column data types, missing value
    counts, and summary statistics in a single simplified structure to
    streamline the initial exploratory data analysis process.

-   `numeric(df, numeric_features)`: Perform exploratory data analysis
    (EDA) on numerical features in a dataset. Generates visualizations
    for specified numerical columns to help with initial exploratory
    analysis. It produces histogram plots to examine distributions,
    correlation plots to identify relationships between features,
    missing values, and other relevant numerical summaries.

-   `categorical_plot(``df: pd.DataFrame, categorical_features, categorical_target)`:
    Creates Altair plots for the specified categorical columns. Creates
    bar charts and pie charts for each features. Also create box plots
    or stacked bar charts for each feature against the target depending
    on if the target is categorical or numerical.

-   `all_distributions(             pd_dataframe: pd.DataFrame,              columns: list = None,             ambiguous_column_types: dict = None) -> None`.
    The main interface for column-level EDA distribution visualizations
    for numeric and categorical columns. Automatically identifies each
    columns data types and routes them to the appropriate plotting
    functions (`function_2` and `function_3`). However, also includes a
    manual overrides for ambiguous columns via explicit user input where
    the default columns data types may be incorrectly represented.

## Get started

You can install this package into your preferred Python environment
using pip:

``` bash
$ pip install eda_simplifier
```

TODO: Add a brief example of how to use the package to this section

To use eda_simplifier in your code:

``` python
>>> import eda_simplifier
>>> eda_simplifier.hello_world()
```

## Contributors

-   Diana Cornescu
-   Johnson Chuang
-   Lavanya Gupta
-   Tiantong Yin

## Copyright

-   Copyright © Diana Cornescu, Johnson Chuang, Lavanya Gupta & Tiantong
    Yin.
-   Free software distributed under the [MIT License](./LICENSE).
