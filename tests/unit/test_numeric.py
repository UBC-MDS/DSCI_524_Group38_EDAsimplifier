import pandas as pd
import numpy as np
import altair as alt

from eda_simplifier.simplify import numeric

def test_numeric():
    # Create dummy data for testing
    np.random.seed(42)
    n = 100
    df = pd.DataFrame({
        'acousticness': np.random.uniform(0, 1, n),
        'energy': np.random.uniform(0, 1, n),
        'instrumentalness': np.random.uniform(0, 1, n),
        'target': np.random.choice([0, 1], n)
    })

    # Artificially introduce missing values for testing
    n = len(df)
    df.loc[df.sample(frac=0.75, random_state=42).index, 'acousticness'] = np.nan
    df.loc[df.sample(frac=0.50, random_state=42).index, 'energy'] = np.nan
    df.loc[df.sample(frac=0.25, random_state=42).index, 'instrumentalness'] = np.nan

    # Call numeric()
    result = numeric(df, 'target')

    # Test that the result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"

    # Test that all expected keys are present
    expected_keys = {'missing_vals', 'box_plot', 'distribution', 'correlation'}
    assert set(result.keys()) == expected_keys, f"Expected keys {expected_keys} but got {set(result.keys())}"

    # Test that each value is an Altair chart object
    for key, value in result.items():
        assert isinstance(value, (alt.Chart, alt.VConcatChart, alt.LayerChart)), f"Value for '{key}' should be an Altair chart"


#if __name__ == "__main__":
#    test_numeric()
#    print("Test passed!")
