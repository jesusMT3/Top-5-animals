import pandas as pd

def import_data(url: str):
    """
    Imports a csv from a url into a pandas dataframe.

    Args:
        url (str): Url to download the csv

    Returns:
        data (pd.DataFrame): Data converted into a pandas dataframe.
    """
    # read data
    data = pd.read_csv(url, delimiter = ",").dropna(axis=1, how='all')
    
    # data treatment
    last_five_cols = data.columns[-5:]
    data[last_five_cols] = data[last_five_cols].astype(str).apply(lambda x: x.str.lower().str.strip())
    data[last_five_cols] = data[last_five_cols].apply(lambda x: x.str.lower().str.strip())
    data["Name"] = data["Name"].apply(lambda x: x.strip())
    
    return data

def make_ranking(data: pd.DataFrame):
    """
    Makes the ranking dataframe of the data. Each row will be given
    5 points for each top 1, 4 points for each top 2, and so on.

    Args:
        data (pd.DataFrame): Must contain five columns called: "1st animal", "2nd animal"... and so on.

    Returns:
        pd.DataFrame: The ranking in descending order.
    """
    
    # ranking dataframe
    last_five_cols = data.columns[-5:]
    all_animals = pd.concat([data[i] for i in last_five_cols])
    unique_animals = all_animals.unique()
    
    values_first = data["1st animal"].value_counts()
    values_second = data["2nd animal"].value_counts()
    values_third = data["3rd animal"].value_counts()
    values_fourth = data["4th animal"].value_counts()
    values_fifth = data["5th animal"].value_counts()
    
    ranking = pd.DataFrame(index = unique_animals)
    votes = all_animals.value_counts()
    ranking["votes"] = votes
    
    values = []
    for animal in unique_animals:
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
            value += 1 * values_fifth[animal]

        values.append(value)
    
    ranking["values"] = values
    ranking = ranking.sort_values(by = "values", ascending = False)
    
    return ranking


def get_distribution(data: pd.DataFrame, parameter: str):
    gender_data = data[parameter].value_counts()
    return gender_data