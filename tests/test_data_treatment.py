# pylint: skip-file

import pandas as pd
from data_treatment import import_data, make_ranking

SHEET_NAME = 'test'
SHEET_ID = '1KCmNGGoHiHm16pI6D14MY_GUdizSpOdJfnQNLMQLDFw'
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Unit tests for import_data()
DATA_ROWS = 6
DATA_COLS = 10

def test_import_data_imports():
    data = import_data(url)
    assert data is not None

def test_import_data_type():
    data = import_data(url)
    assert isinstance(data, pd.DataFrame)

def test_import_data_size():
    data = import_data(url)
    assert len(data) == DATA_ROWS
    assert len(data.columns) == DATA_COLS

# Unit tests for make_ranking()
RANKING_ROWS = 10
RANKING_COLS = 2

def test_make_ranking_imports():
    data = import_data(url)
    ranking = make_ranking(data)
    assert ranking is not None

def test_make_ranking_type():
    data = import_data(url)
    ranking = make_ranking(data)
    assert isinstance(ranking, pd.DataFrame)

def test_make_ranking_size():
    data = import_data(url)
    ranking = make_ranking(data)
    assert len(ranking) == RANKING_ROWS
    assert len(ranking.columns) == RANKING_COLS

def test_make_ranking_filter():
    data = import_data(url)
    ranking = make_ranking(data, custom_filter = ("Gender", "Male"))
    assert len(ranking) == RANKING_ROWS / 2