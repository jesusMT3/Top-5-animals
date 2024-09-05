from data_treatment import *
from plots import *

def main():
    # get google sheets database
    sheet_name = 'top-5-animals'
    sheet_id = '1XLO-q3zrwgsAbITzBbIgICT9X61GZ8c4LX_ubsE2JCo'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    # import data
    data = import_data(url)
    
    # distributions
    gender_distribution = get_distribution(data, "Gender")
    country_distribution = get_distribution(data, "Country")
    age_distribution = get_distribution(data, "Age")
    
    # get ranking dataframe
    ranking = make_ranking(data)
    
    # get first 15 animals
    ranking = ranking[0:15]
    
    # plot
    # plot_ranking(ranking)

if __name__ == "__main__":
    main()