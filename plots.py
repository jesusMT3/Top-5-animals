import matplotlib.pyplot as plt
import pandas as pd

def plot_ranking(ranking: pd.DataFrame):
    fig, ax = plt.subplots(figsize = (12, 9))
    ax.bar(ranking.index, ranking["values"])
    plt.xticks(rotation = 45)
    
    plt.show()