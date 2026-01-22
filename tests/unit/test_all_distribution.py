from eda_simplifier.simplify import all_distributions
import pandas as pd
import pytest


def test_all_distributions_basic():
    """Test that all_distributions returns correct structure with basic input."""
    df = pd.DataFrame({"rank": [1, 2, 5], "genre": ["Pop", "Jazz", "Rock"]})
    result = all_distributions(df, "rank", categorical_target=False)

    assert isinstance(result, dict)
    assert "numeric" in result
    assert "categorical" in result


def test_all_distributions_with_ambiguous_override():
    """Test that all_distributions applies ambiguous_column_types overrides."""
    df = pd.DataFrame({"year": [2020, 2021, 2022], "genre": ["Pop", "Rock", "Jazz"]})
    result = all_distributions(
        df,
        "genre",
        categorical_target=True,
        ambiguous_column_types={"numeric": [], "categorical": ["year"]},
    )

    assert isinstance(result, dict)
    assert "numeric" in result
    assert "categorical" in result


def test_all_distributions_empty_dataframe():
    """Test that empty dataframe overrides raise a ValueError."""
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        all_distributions(df, "target", categorical_target=False)


def test_all_distributions_with_categorical_features():
    """Test that all_distributions filters via categorical_features parameter."""
    df = pd.DataFrame(
        {
            "genre": [
                "Pop",
                "Pop",
                "Rock",
                "Jazz",
                "Jazz",
                "Jazz",
                "Hip-Hop",
                "Pop",
                "Rock",
                "Indie",
            ],
            "popularity": [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
            "is_explicit": [
                "Explicit",
                "Clean",
                "Clean",
                "Clean",
                "Explicit",
                "Clean",
                "Explicit",
                "Clean",
                "Clean",
                "Clean",
            ],
            "track_id": [f"id_{i}" for i in range(10)],
        }
    )
    result = all_distributions(
        df, "popularity", categorical_target=False, categorical_features=["genre"]
    )

    assert isinstance(result, dict)
    assert "numeric" in result
    assert "categorical" in result


def test_all_distributions_with_max_categories():
    """Test that all_distributions accepts max_categories parameter."""
    df = pd.DataFrame({"value": [1, 2, 3, 4, 5], "category": ["A", "B", "C", "D", "E"]})
    result = all_distributions(df, "value", categorical_target=False, max_categories=3)

    assert isinstance(result, dict)
    assert "numeric" in result
    assert "categorical" in result
