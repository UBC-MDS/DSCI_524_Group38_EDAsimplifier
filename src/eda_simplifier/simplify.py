"""
A module that simplifies the EDA process.

This module contains functions that consolidate many of the steps used in the
preliminary EDA process for any given pandas DataFrame. It uses Altair, which is
powerful but verbose, so some functions abstract common patterns and apply smart 
defaults to streamline EDA exploration.
"""
import pandas as pd
import altair as alt

def dataset_overview(df):
    """
    Generates a consolidated exploratory summary of the dataset.

    This function provides a single, high level overview of the dataset by
    combining commonly used exploratory data analysis (EDA) outputs such as
    dataset dimensions, column data types, missing value counts, and
    descriptive statistics. It is intended to simplify the initial EDA
    process by replacing multiple pandas method calls (e.g., .info(),
    .describe(), .shape) with one function.

    Parameters
    ----------
    df : pandas.DataFrame
        A pandas dataFrame containing the dataset to be summarized.

    Returns
    -------
    dict
        A dictionary with the following fixed structure:
        - "shape" : tuple[int, int]
            Number of rows and columns in the DataFrame.
        - "columns" : list[str]
            List of column names, in the order they appear in the DataFrame.
        - "dtypes" : dict[str, str]
            Mapping of column names to their pandas data types (as strings).
        - "missing_values" : dict[str, int]
            Count of missing (NaN) values per column.
        - "summary_statistics" : dict[str, pandas.Series]
            Descriptive statistics for numeric columns only, as returned by
            `pandas.DataFrame.describe()`.

    Raises
    ------
    TypeError
        If the input provided is not a pandas dataFrame.

    Notes
    -----
    - This function does not modify the input DataFrame.
    - If the DataFrame is empty, all returned values will be empty but valid.
    - If the DataFrame contains no numeric columns, "summary_statistics"
      will be an empty dictionary.
    - The returned dictionary follows a fixed structure to support
      deterministic unit testing.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "artist": ["A", "B", "C"],
    ...     "popularity": [80, 75, None],
    ...     "danceability": [0.8, 0.6, 0.9]
    ... })
    >>> dataset_overview(df)
    {
        "shape": (3, 3),
        "columns": ["artist", "popularity", "danceability"],
        "dtypes": {
            "artist": "object",
            "popularity": "float",
            "danceability": "float"
        },
        "missing_values": {
            "artist": 0,
            "popularity": 1,
            "danceability": 0
        },
        "summary_statistics": {
            "popularity": {...},
            "danceability": {...}
        }
    }
    """
    #Input validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    #Baseline components
    shape = df.shape
    columns = list(df.columns)
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
    missing_values = df.isna().sum().to_dict()

    #Summary statistics for numeric columns only
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        summary_statistics = {}
    else:
        summary_statistics = {
            col: numeric_df[col].describe()
            for col in numeric_df.columns
        }

    return {
        "shape": shape,
        "columns": columns,
        "dtypes": dtypes,
        "missing_values": missing_values,
        "summary_statistics": summary_statistics,
    }


def numeric(df, numeric_features):
    """
    Perform exploratory data analysis (EDA) on numerical features in a dataset.

    This function generates visualizations for specified numerical columns to
    help with initial exploratory analysis. It produces histogram plots to
    examine distributions, correlation plots to identify relationships between
    features, missing values, and other relevant numerical summaries.

    Parameters
    ----------
    df : pandas.DataFrame
        A pandas DataFrame containing the dataset to be analyzed.
    numeric_features : list of str
        A list of column names representing the numerical features to analyze.

    Returns
    -------
    dict
        A dictionary containing:
        - plots: Altair figures for distribution plots, correlation plots, 
        missing values, and potential outliers

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame or numeric_features is not a list

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "artist": ["A", "B", "C", "D"],
    ...     "popularity": [80, 75, 90, 85],
    ...     "danceability": [0.8, 0.6, 0.9, 0.7],
    ...     "energy": [0.7, 0.8, 0.6, 0.9]
    ... })
    >>> result = numeric(df, ["popularity", "danceability", "energy"])
    >>> result.keys()
    dict_keys(['histograms', 'correlation_plot', 'missing_vals', 'outliers'])
    """
    pass
    
def categorical_plot(
        df: pd.DataFrame, 
        target_column: str,
        categorical_target: bool,
        max_categories:int = 10,
        categorical_features: list = None
        ) -> list:
    """
    Perform EDA on categorical columns in a dataset.

    
    This function creates Altair plots for the specified columns, assuming 
    them to contain categorical data. It creates sorted horizontal bar charts 
    to show the frequency and the proportion of each categories. Also create
    box plots for features vs target if the target is numerical, or stacked
    bar charts if the target is categorical.
   
    Parameters
    ----------
    df : pandas.DataFrame
        A pandas DataFrame containing the dataset
    target_column: str
        The name of the target column.
    categorical_target : bool
        A boolean value indicating if the target column is categorical or not.
    max_categories: int
        The maximum categories to plot for high cardinality features
    categorical_features : list
        A list of strings containing column names of the categorical features.
        If this is not passed, keep all

    Returns
    -------
    list
        A list of Altair plot objects of all the plots created

    Raises
    ------
    TypeError
        If df is not a dataframe, target_column is not a string, or 
        categorical_features is not a list
    ValueError
        If df is empty, target_column is not in the DataFrame, or 
        categorical_features is empty or contains columns not in the DataFrame

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "artist": ["A", "B", "C", "D"],
    ...     "popularity": [80, 75, 90, 85],
    ...     "danceability": [0.8, 0.6, 0.9, 0.7],
    ...     "energy": [0.7, 0.8, 0.6, 0.9]
    ... })
    >>> plots = categorical_plot(df, 'popularity', False, categorical_features=["artist"])
    """
    # Input Validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a dataframe")

    if df.empty:
        raise ValueError("df must not be empty")

    if not isinstance(target_column, str):
        raise TypeError("target_column must be a string")

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataframe")

    if categorical_features is None or len(categorical_features) == 0:
        categorical_features = [col for col in df.columns if col != target_column]

    if not isinstance(categorical_features, list):
        raise TypeError("categorical_features must be a list")

    if len(categorical_features) == 0:
        raise ValueError("No categorical features to plot")

    for feature in categorical_features:
        if feature not in df.columns:
            raise ValueError(f"Column '{feature}' not found in dataframe")
    
    plots = []
    for feature in categorical_features:
        # filter based on class count limit
        top_features = df[feature].value_counts().nlargest(max_categories).index.tolist()
        df = df[df[feature].isin(top_features)].copy()
        
        # sorted horizontal bar chart
        bar_chart = alt.Chart(df).mark_bar().encode(
            y=alt.Y(f"{feature}:N", sort='-x', title=feature),
            x=alt.X("count():Q"),
        ).properties(
            title=f"Frequency count of {feature}"
        )
        
        plots.append(bar_chart)
        
        if categorical_target:
            vs_target = alt.Chart(df).mark_bar().encode(
                y=alt.Y(f"{feature}:N", sort='-x', title=feature),
                x=alt.X("count():Q"),
                color=alt.Color(f"{target_column}:N")
            ).properties(
                title=f"{feature} vs {target_column}",
            )
        else:
            vs_target = alt.Chart(df).mark_boxplot().encode(
                y=alt.Y(f"{feature}:N", sort='-x', title=feature),
                x=alt.X(f"{target_column}:Q", title=target_column),
                color=alt.Color(f"{feature}:N")
            ).properties(
                title=f"{feature} vs {target_column}",
            )
        
        plots.append(vs_target)
    return plots


def all_distributions(
            pd_dataframe: pd.DataFrame, 
            target_column: str,
            categorical_target: bool,
            max_categories: int = 10,
            categorical_features: list = None,
            ambiguous_column_types: dict = None) -> None:
    """
    Generate distribution visualizations (e.g., histograms and bar charts) for numeric 
    and categorical columns in a DataFrame.

    This is the main function for column-level EDA distribution visualizations.
    The function automatically infers whether columns are numeric or categorical. 
    Allows manual overrides for ambiguous columns, ambiguous columns are cases where 
    a numeric datatype column should be treated as categorical or vice versa.

    Parameters
    ----------
    pd_dataframe : pandas.DataFrame
        Input DataFrame containing the data to be analyzed. Expects a tidy dataframe (one 
        value or string per cell) but can handle some common messy data issue such as incorrect datatypes 
        via ambiguous_column_types parameter.

    target_column: str
        The name of the target column. Funneled to all subfunctions.
        
    categorical_target : bool
        A boolean value indicating if the target column is categorical or not.

    max_categories: int
        The maximum categories to plot for high cardinality features. Funneled to categorical_plot function

    categorical_features : list
        Subset of columns to use for categorical plots. If this is not passed, keep all.
        Subset of columns to include in the analysis. Invalid or non-existent column names are ignored.

    ambiguous_column_types: dict, optional
        Dictionary specifying column type overrides for ambiguous cases.
        Expected keys are ``"numeric"`` and ``"categorical"``, with values
        being lists of column names to force into each category. If a column appears in both lists,
        will raise a ValueError. Invalid or non-existent column names are ignored.

        Example:
            ambiguous_column_types = {"numeric" : ['year'], "categorical": ['zip_code]}
                                    
    Returns
    -------
    dict
        This function produces distribution plots as a side effect and returns a 
        dictionary of plots types: {"numeric" : cat_plots, "categorical": numeric_plots}. 
        Currently the categorical_plots contains plots in the form of an appended plot 
        object / list, and numeric_plots contains plots organized in a dictionary according to plot type.
        
    """
    subset_df = _ambiguous_columns_split(pd_dataframe, target_column, ambiguous_column_types)

    numeric_plots = numeric(subset_df["numeric"], target_column)

    categorical_plots = categorical_plot(subset_df["categorical"], target_column, 
                    categorical_target = categorical_target,
                    max_categories = max_categories,
                    categorical_features = categorical_features)
    
    return {"numeric" : numeric_plots, "categorical": categorical_plots} 

def _ambiguous_columns_split(pd_dataframe: pd.DataFrame,
                            target_column: str,
                            ambiguous_column_types: dict = None) -> dict:
    """
    Separates numeric and categorical columns for a pandas Dataframe, 
    and applies overrides for ambiguous cases via input. Hidden function used purely for 
    all_distributions function. 

    This function automatically classifies DataFrame columns as numeric or categorical
    based on their data types. Supports manual overrides when automatic 
    classification is incorrect (e.g., a numeric zip code that should be treated as categorical).

    Parameters
    ----------
    pd_dataframe : pandas.DataFrame
        Input DataFrame to separate into numeric and categorical columns.

    target_column: str
        The name of the target column. Regardless of dtype, target column is included
        in both numeric and categorical outputs.

    ambiguous_column_types : dict, optional
        Dictionary specifying column type overrides for ambiguous cases.
        Expected keys are "numeric" and "categorical", each containing a list of 
        column names to force into that category. Invalid or non-existent column 
        names are silently ignored.

        Numeric definded as: int, float, and complex, 
            including int/float 32/64, np.number and boolean columns too (Pandas behaviour).
        Categorical definded as: Non-numeric columns, including object, string,
            datetime, and categorical dtypes. 

        Example:
            ambiguous_column_types = {"numeric": ["year"], "categorical": ["zip_code"]}

    Returns
    -------
    dict
        A dictionary with keys "numeric" and "categorical", each containing a filtered
        DataFrame with only the columns of that type.
    
    Raises
    ------
    ValueError
        If the input DataFrame is empty.
    ValueError
        If a column is specified in both "numeric" and "categorical" lists in ambiguous_column_types.
    """
    if pd_dataframe.empty:
        raise ValueError("Input DataFrame cannot be empty")
        
    # Default to empty lists if no overrides provided
    if ambiguous_column_types is None:
        ambiguous_column_types = {"numeric": [], "categorical": []}

    # Split column referances and ignores invalid / non-existent columns 
    ambiguously_numeric = set(ambiguous_column_types["numeric"]).intersection(pd_dataframe.columns)
    ambiguously_categorical = set(ambiguous_column_types["categorical"]).intersection(pd_dataframe.columns)

    # Check for conflicts
    overlap = ambiguously_numeric & ambiguously_categorical
    if overlap:
        raise ValueError(f"Column(s) {overlap} cannot be both 'numeric' and 'categorical'")

    # Get default dtype columns
    numeric_cols = set(pd_dataframe.select_dtypes(include="number").columns)
    categorical_cols = set(pd_dataframe.select_dtypes(exclude="number").columns)

    # Add relevent ambiguous set then ambiguous/false set
    numeric_overriden = (numeric_cols | ambiguously_numeric) - ambiguously_categorical
    categorical_overriden = (categorical_cols | ambiguously_categorical) - ambiguously_numeric

    # Always include target column in both
    numeric_overriden.add(target_column)
    categorical_overriden.add(target_column)
    
    # Create filtered dataframes
    numeric_df = pd_dataframe[list(numeric_overriden)]
    categorical_df = pd_dataframe[list(categorical_overriden)]

    return {"numeric": numeric_df, "categorical": categorical_df}

