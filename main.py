import pandas as pd
# https://docs.google.com/spreadsheets/d/1XLO-q3zrwgsAbITzBbIgICT9X61GZ8c4LX_ubsE2JCo/edit?usp=sharing

sheet_name = 'top-5-animals'
sheet_id = '1XLO-q3zrwgsAbITzBbIgICT9X61GZ8c4LX_ubsE2JCo'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

data = pd.read_csv(url)
print(data)

