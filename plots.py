import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colormaps

def plot_ranking(ranking: pd.DataFrame):
    """
    Draws a bar plot of the ranking dataframe.

    Args:
        ranking (pd.DataFrame)
    """
    # Define custom colors for the bars
    gold = '#FFD700'
    silver = '#C0C0C0'
    bronze = '#CD7F32'
    rest = '#00CC66'
    all_colors = [gold, silver, bronze] + [rest] * (len(ranking) - 3)

    fig, ax = plt.subplots(figsize=(12, 9))
    plt.xticks(rotation=45)
    ax2 = ax.twinx()
    ax.bar(ranking.index, ranking["values"], color=all_colors)
    ax2.plot(ranking.index, ranking["votes"], 'or')
    
    plt.show()


def plot_gender(gender_distribution: pd.DataFrame):
    """
    Draws a bar plot of the gender distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    
    raise NotImplementedError


def plot_country(country_distribution: pd.DataFrame):
    """
    Draws a bar plot of the country distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    raise NotImplementedError


def plot_age(age_distribution: pd.DataFrame):
    """
    Draws a bar plot of the rage distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    raise NotImplementedError