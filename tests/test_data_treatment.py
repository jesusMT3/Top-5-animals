from data_treatment import import_data, make_ranking
import pandas as pd

sheet_name = 'test'
sheet_id = '1KCmNGGoHiHm16pI6D14MY_GUdizSpOdJfnQNLMQLDFw'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

def test_import_data():
    data = import_data(url)
    # import_data imports
    assert data is not None
    
    # import data returns a dataframe
    assert type(data) == pd.DataFrame
    
def test_contents_import_data():
    data = import_data(url)
    # import data returns the desired rows
    assert len(data) == 6
    
    # import data returns the desired columns
    assert len(data.columns) == 10
    

def test_make_ranking():
    data = import_data(url)
    ranking = make_ranking(data)
    
    # ranking returns 
    assert ranking is not None
    
    # ranking is a dataframe
    assert type(ranking) == pd.DataFrame