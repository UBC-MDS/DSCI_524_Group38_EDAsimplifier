from eda_simplifier.simplify import _ambiguous_columns_split
import pandas as pd
import pytest
 
#TO-DO add one-line test documentation 

 # Sunny day test cases (basic functionality works as intented):
def test_basic_separation():
    df = pd.DataFrame({
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)]
    })
    result = _ambiguous_columns_split(df)

    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit'}

def test_override_numeric_to_categorical():
    df = pd.DataFrame({'year': [2020, 2021, 2022], 
                       'genre': ['Pop', 'Pop', 'Rock']})
    result = _ambiguous_columns_split(df, {'numeric': [], 'categorical': ['year']})

    # BOTH that year IS in categorical and NOT in numeric
    assert 'year' in result['categorical'].columns
    assert 'year' not in result['numeric'].columns

def test_override_categorical_to_numeric():
    df = pd.DataFrame({'rank': ["1", "2", "5"], 
                       'genre': ['Pop', 'Jazz', 'Rock']})
    result = _ambiguous_columns_split(df, {'numeric': ['rank'], 'categorical': []})
    # BOTH that rank IS in numeric and NOT in categorical
    assert 'rank' in result['numeric'].columns
    assert 'rank' not in result['categorical'].columns

def test_none_ambiguous_columns():
    df = {
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)],
        'rank': ["1", "2", "5","3", "4", "6", "7", "8", "9", "10"]}
    result = _ambiguous_columns_split(df, None)
    
    #if None passed, all ambiguous should go to their default dtype label
    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit', 'rank'}

# Error handling:
def test_conflict_raises_error():
    df = pd.DataFrame({'rank': ["1", "2", "5"], 
                       'genre': ['Pop', 'Jazz', 'Rock']})
    with pytest.raises(ValueError):
        _ambiguous_columns_split(df, {'numeric': ['rank'], 'categorical': ['rank']})

# Edge cases:
def test_invalid_columns_ignored():
    df = {
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)]}
    result = _ambiguous_columns_split(df, {'numeric': ['rank',], 'categorical': ['nonexistent_col']})
    
    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit'}
    assert 'rank' not in result['numeric'].columns
    assert 'nonexistent_col' not in result['categorical'].columns