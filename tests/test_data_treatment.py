# pylint: skip-file

import pandas as pd
from data_treatment import import_data, make_ranking

SHEET_NAME = 'test'
SHEET_ID = '1KCmNGGoHiHm16pI6D14MY_GUdizSpOdJfnQNLMQLDFw'
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Unit tests for import_data()
def test_import_data_imports():
    data = import_data(url)
    assert data is not None

def test_import_data_type():
    data = import_data(url)
    assert isinstance(data, pd.DataFrame)

def test_import_data_row_count():
    data = import_data(url)
    assert len(data) == 6

def test_import_data_column_count():
    data = import_data(url)
    assert len(data.columns) == 10

def test_import_data_content():
    data = import_data(url)
    assert data.loc[2, "Age"] == 23
    assert data.loc[3, "Country"] == "Norway"

# Unit tests for make_ranking()
def test_make_ranking_imports():
    data = import_data(url)
    ranking = make_ranking(data)
    assert ranking is not None

def test_make_ranking_type():
    data = import_data(url)
    ranking = make_ranking(data)
    assert isinstance(ranking, pd.DataFrame)
