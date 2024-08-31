import pandas as pd
import matplotlib.pyplot as plt

# get google sheets database
sheet_name = 'top-5-animals'
sheet_id = '1XLO-q3zrwgsAbITzBbIgICT9X61GZ8c4LX_ubsE2JCo'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# read data
data = pd.read_csv(url)

# data treatment
last_five_cols = data.columns[-5:]
data[last_five_cols] = data[last_five_cols].apply(lambda x: x.str.lower().str.strip())
data["Name"] = data["Name"].apply(lambda x: x.strip())

all_animals = pd.concat([data[i] for i in last_five_cols]).unique()

# ranking dataframe
ranking = pd.DataFrame(index = all_animals)
values_first = data["1st animal"].value_counts()
values_second = data["2nd animal"].value_counts()
values_third = data["3rd animal"].value_counts()
values_fourth = data["4th animal"].value_counts()
values_fifth = data["5th animal"].value_counts()

values = []
for animal in all_animals:
    value = 0
    if animal in values_first:
        value += 5 * values_first[animal]
    if animal in values_second:
        value += 4 * values_second[animal]
    if animal in values_third:
        value += 3 * values_third[animal]
    if animal in values_fourth:
        value += 2 * values_fourth[animal]
    if animal in values_fifth:
        value += values_fifth[animal]

    values.append(value)
ranking["values"] = values

# get first 15 animals
ranking = ranking.sort_values(by = "values", ascending = False)
ranking = ranking[0:15]

# plot ranking
fig, ax = plt.subplots(figsize = (12, 9))
ax.bar(ranking.index, ranking["values"])
plt.xticks(rotation = 45)

plt.show()