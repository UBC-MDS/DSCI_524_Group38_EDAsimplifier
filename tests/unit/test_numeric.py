import pandas as pd
import numpy as np
import altair as alt
import pytest

from eda_simplifier.simplify import numeric


def test_numeric():
    # Create dummy data for testing
    np.random.seed(42)
    n = 100
    df = pd.DataFrame(
        {
            "acousticness": np.random.uniform(0, 1, n),
            "energy": np.random.uniform(0, 1, n),
            "instrumentalness": np.random.uniform(0, 1, n),
            "target": np.random.choice([0, 1], n),
        }
    )

    # Artificially introduce missing values for testing
    n = len(df)
    df.loc[df.sample(frac=0.75, random_state=42).index, "acousticness"] = np.nan
    df.loc[df.sample(frac=0.50, random_state=42).index, "energy"] = np.nan
    df.loc[df.sample(frac=0.25, random_state=42).index, "instrumentalness"] = np.nan

    # Call numeric()
    result = numeric(df, "target")

    # Test that the result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    # Test that all expected keys are present
    expected_keys = {"missing_vals", "box_plot", "distribution", "correlation"}
    assert (
        set(result.keys()) == expected_keys
    ), f"Expected keys {expected_keys} but got {set(result.keys())}"

    # Test that each value is an Altair chart object
    for key, value in result.items():
        assert isinstance(
            value, (alt.Chart, alt.VConcatChart, alt.LayerChart)
        ), f"Value for '{key}' should be an Altair chart"


def test_nonexistent_target():
    # Test that ValueError is raised when target column doesn't exist in DataFrame
    df = pd.DataFrame(
        {"feature1": [1, 2, 3], "feature2": [4, 5, 6], "target": [0, 1, 0]}
    )

    with pytest.raises(ValueError):
        numeric(df, target="nonexistent_column")


def test_df_not_dataframe():
    # Test that TypeError is raised when df is not a pandas DataFrame
    with pytest.raises(TypeError):
        numeric([1, 2, 3], target="target")

    with pytest.raises(TypeError):
        numeric({"a": 1, "b": 2}, target="target")

    with pytest.raises(TypeError):
        numeric(None, target="target")


def test_target_not_string():
    # Test that TypeError is raised when target is not a string
    df = pd.DataFrame(
        {"feature1": [1, 2, 3], "feature2": [4, 5, 6], "target": [0, 1, 0]}
    )

    with pytest.raises(TypeError):
        numeric(df, target=123)

    with pytest.raises(TypeError):
        numeric(df, target=["target"])

    with pytest.raises(TypeError):
        numeric(df, target=None)


def test_empty_dataframe():
    # Test behavior when DataFrame is empty
    df = pd.DataFrame({"feature1": [], "feature2": [], "target": []})
    result = numeric(df, target="target")

    # Check that result is still a dictionary with expected keys
    assert isinstance(result, dict)
    expected_keys = {"missing_vals", "box_plot", "distribution", "correlation"}
    assert set(result.keys()) == expected_keys


# if __name__ == "__main__":
#    test_nonexistent_target()
#    test_df_not_dataframe()
#    test_target_not_string()
#    test_empty_dataframe()
#    test_numeric()
#    print("Test passed!")
