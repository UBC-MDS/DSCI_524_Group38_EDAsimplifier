from eda_simplifier.simplify import categorical_plot
import pandas as pd
import pytest
import altair as alt

def test_categorical_plot():
    data = {
        'genre': ['Pop', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Indie'],
        'popularity': [88, 92, 55, 30, 25, 35, 70, 95, 40, 60],
        'is_explicit': ['Explicit', 'Clean', 'Clean', 'Clean', 'Explicit', 'Clean', 'Explicit', 'Clean', 'Clean', 'Clean'],
        'track_id': [f'id_{i}' for i in range(10)]
    }
    df = pd.DataFrame(data)

    plots = categorical_plot(df, ['genre'], 'popularity', categorical_target=False)
    
    assert isinstance(plots, list)
    assert len(plots) == 2, "Should return a bar chart and a box plot"

    # bar chart
    bar_chart = plots[0].to_dict()
    assert bar_chart['mark']['type'] == 'bar'
    assert bar_chart['encoding']['y']['field'] == 'genre'
    assert 'count' in str(bar_chart['encoding']['x'])
    assert 'sort' in bar_chart['encoding']['y'], "y should be sorted"

    # box plot
    box_plot = plots[1].to_dict()
    # LLM revision: Altair boxplot marks can be strings or dicts depending on version
    mark_type = box_plot['mark']['type'] if isinstance(box_plot['mark'], dict) else box_plot['mark']
    assert mark_type == 'boxplot'
    assert box_plot['encoding']['x']['field'] == 'popularity'
    assert box_plot['encoding']['y']['field'] == 'genre'

    plots2 = categorical_plot(df, ['genre'], 'is_explicit', categorical_target=True)
    
    # stacked bar chart
    stacked = plots2[1].to_dict()
    assert stacked['mark']['type'] == 'bar'
    assert stacked['encoding']['color']['field'] == 'is_explicit'
    assert stacked['encoding']['y']['field'] == 'genre'


    # LLM revision: test max categories
    limit = 3
    plots_limit = categorical_plot(df, ['track_id'], 'popularity', False, max_categories=limit)
    plot_data = plots_limit[0].data
    if plot_data is not None:
        assert plot_data['track_id'].nunique() <= limit
    else:
        # If data is embedded in the JSON spec
        values = plots_limit[0].to_dict()['data']['values']
        unique_ids = len(set(v['track_id'] for v in values))
        assert unique_ids <= limit

    plot_empty = categorical_plot(df, [], 'popularity', False)
    assert isinstance(plot_empty, list)
    assert len(plot_empty) == 0
