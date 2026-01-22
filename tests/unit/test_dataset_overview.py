import pandas as pd
import pytest

from eda_simplifier.simplify import dataset_overview


def test_raises_type_error_for_non_dataframe():
    """Non-DataFrame input should raise TypeError."""
    with pytest.raises(TypeError):
        dataset_overview("not a dataframe")


def test_returns_expected_keys():
    """Returned dictionary should have the expected fixed structure."""
    df = pd.DataFrame({"col_a": [1, 2], "col_b": [3, 4]})
    result = dataset_overview(df)

    assert set(result.keys()) == {
        "shape",
        "columns",
        "dtypes",
        "missing_values",
        "summary_statistics",
    }


def test_empty_dataframe_returns_empty_structures():
    """Empty DataFrame should return empty but valid outputs."""
    df = pd.DataFrame()
    result = dataset_overview(df)

    assert result["shape"] == (0, 0)
    assert result["columns"] == []
    assert result["dtypes"] == {}
    assert result["missing_values"] == {}
    assert result["summary_statistics"] == {}


def test_dataframe_with_no_numeric_columns():
    """No numeric columns should produce empty summary_statistics."""
    df = pd.DataFrame(
        {
            "col_a": ["x", "y", "z"],
            "col_b": ["a", "b", "c"],
        }
    )
    result = dataset_overview(df)

    assert result["summary_statistics"] == {}
    assert result["columns"] == ["col_a", "col_b"]


def test_numeric_columns_include_summary_statistics():
    """Numeric columns should be summarized correctly."""
    df = pd.DataFrame(
        {
            "col_a": [1, 2, None],
            "col_b": [4.0, 5.0, 6.0],
        }
    )
    result = dataset_overview(df)

    assert "col_a" in result["summary_statistics"]
    assert "col_b" in result["summary_statistics"]

    # describe() to count non-missing values
    assert result["summary_statistics"]["col_a"]["count"] == 2
