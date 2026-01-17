from eda_simplifier.simplify import _ambiguous_columns_split
import pandas as pd
import pytest
 
 # Sunny day test cases (basic functionality works as intented):
def test_basic_separation():
    """Test that ambiguous columns are correctly split into numeric and categorical."""
    df = pd.DataFrame({
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)]
    })
    target_column = 'track_id'
    result = _ambiguous_columns_split(df, target_column)

    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit', "track_id"}

def test_override_numeric_to_categorical():
    '''Test that ambiguous columns can be overridden to categorical.'''
    df = pd.DataFrame({'year': [2020, 2021, 2022], 
                       'genre': ['Pop', 'Pop', 'Rock']})
    target_column = 'genre'
    result = _ambiguous_columns_split(df, target_column, {'numeric': [], 'categorical': ['year']})

    # BOTH that year IS in categorical and NOT in numeric
    assert 'year' in result['categorical'].columns
    assert 'year' not in result['numeric'].columns

def test_override_categorical_to_numeric():
    '''Test that ambiguous columns can be overridden to numeric.'''
    df = pd.DataFrame({'rank': ["1", "2", "5"], 
                       'genre': ['Pop', 'Jazz', 'Rock']})
    target_column = 'genre'
    result = _ambiguous_columns_split(df, target_column, {'numeric': ['rank'], 'categorical': []})
    
    # BOTH that rank IS in numeric and NOT in categorical
    assert 'rank' in result['numeric'].columns
    assert 'rank' not in result['categorical'].columns

def test_none_ambiguous_columns():
    '''Test that passing None for ambiguous columns uses default behavior.'''
    df = pd.DataFrame({
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)],
        'rank': ["1", "2", "5","3", "4", "6", "7", "8", "9", "10"]})
    result = _ambiguous_columns_split(df, "track_id", None)
    
    #if None passed, all ambiguous should go to their default dtype label
    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit', 'rank', "track_id"}

# Error handling:
def test_conflict_raises_error():
    '''Test that conflicting overrides raise a ValueError.'''
    df = pd.DataFrame({'rank': ["1", "2", "5"], 
                       'genre': ['Pop', 'Jazz', 'Rock']})
    with pytest.raises(ValueError):
        _ambiguous_columns_split(df, "genre", {'numeric': ['rank'], 'categorical': ['rank']})

# Edge cases:
def test_invalid_columns_ignored():
    '''Test that invalid column names are ignored.'''
    df = pd.DataFrame({
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [i for i in range(10)]})
    result = _ambiguous_columns_split(df, "popularity", {'numeric': ['rank',], 'categorical': ['nonexistent_col']})
    
    assert set(result['numeric'].columns) == {'popularity', 'track_id'}
    assert set(result['categorical'].columns) == {'genre', 'is_explicit', "popularity"}
    assert 'rank' not in result['numeric'].columns
    assert 'nonexistent_col' not in result['categorical'].columns