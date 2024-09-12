"""
Module to store all the code that build the plots for the data.
"""
import pandas as pd
import matplotlib.pyplot as plt

def plot_ranking(ranking: pd.DataFrame):
    """
    Draws a bar plot of the ranking dataframe.

    Args:
        ranking (pd.DataFrame)
    """
    # custom colors for the bars
    gold = '#FFD700'
    silver = '#C0C0C0'
    bronze = '#CD7F32'
    rest = '#00CC66'
    all_colors = [gold, silver, bronze] + [rest] * (len(ranking) - 3)

    _, ax = plt.subplots(figsize=(12, 9))
    plt.xticks(rotation=45)

    ax.bar(ranking.index, ranking["values"], color=all_colors)

    max_values = ranking["values"].max()
    max_votes = ranking["votes"].max()
    scaling_factor = 0.33 * max_values / max_votes
    rescaled_votes = ranking["votes"] * scaling_factor
    ax.bar(ranking.index, rescaled_votes, color='gray', alpha=0.7)

    plt.show()


def plot_gender(gender_distribution: pd.DataFrame):
    """
    Draws a pie plot of the gender distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    _, ax = plt.subplots(figsize=(12, 9))
    ax.pie(x = gender_distribution, labels = gender_distribution.index)
    ax.legend()

    plt.show()


def plot_country(country_distribution: pd.DataFrame):
    """
    Draws a pie plot of the country distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    _, ax = plt.subplots(figsize=(12, 9))
    ax.pie(x = country_distribution, labels = country_distribution.index)
    ax.legend()

    plt.show()


def plot_age(age_distribution: pd.DataFrame):
    """
    Draws a bar plot of the age distribution in the data.

    Args:
        ranking (pd.DataFrame)
    """
    _, ax = plt.subplots(figsize=(12, 9))
    ax.bar(age_distribution.index, age_distribution)

    plt.show()
