import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colormaps

def plot_ranking(ranking: pd.DataFrame):
    """
    Draws a bar plot of the ranking database.

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
    ax.bar(ranking.index, ranking["values"], color=all_colors)
    plt.xticks(rotation=45)
    
    plt.show()