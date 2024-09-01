import matplotlib.pyplot as plt
from data_treatment import *

def main():
    # get google sheets database
    sheet_name = 'top-5-animals'
    sheet_id = '1XLO-q3zrwgsAbITzBbIgICT9X61GZ8c4LX_ubsE2JCo'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    # import data
    data = import_data(url)
    
    # get ranking dataframe
    ranking = make_ranking(data)
    
    # get first 15 animals
    ranking = ranking[0:15]
    
    # plot ranking
    fig, ax = plt.subplots(figsize = (12, 9))
    ax.bar(ranking)
    plt.xticks(rotation = 45)

    plt.show()

if __name__ == "__main__":
    main()