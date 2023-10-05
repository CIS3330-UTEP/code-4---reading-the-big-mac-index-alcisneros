import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file) 
year = 2005
country_code= "SWE"

def get_big_mac_price_by_year(year,country_code):
    get_big_mac_price_by_year =f"((date >= '{year}-01-01' and date <= '{year}-12-31') and iso_a3 == '{country_code.upper()}')"
    df_result_year = df.query(get_big_mac_price_by_year)
    price_by_year_mean_round =round(df_result_year['dollar_price'].mean(),2)
    return price_by_year_mean_round
    
def get_big_mac_price_by_country(country_code):
    get_big_mac_price_by_country = f"(iso_a3 == '{country_code.upper()}')"
    df_result_country = df.query(get_big_mac_price_by_country)
    price_by_country_mean_round = round(df_result_country['dollar_price'].mean(),2)
    return price_by_country_mean_round

def get_the_cheapest_big_mac_price_by_year(year):
    get_the_cheapest_big_mac_price_by_year = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_results_min = df.query(get_the_cheapest_big_mac_price_by_year)
    index_min_value = (df_results_min['dollar_price'].idxmin())
    row = df_results_min.loc[index_min_value]
    results = f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"
    return results

def get_the_most_expensive_big_mac_price_by_year(year):
    get_the_most_expensive_big_mac_price_by_year = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_results_max = df.query(get_the_most_expensive_big_mac_price_by_year)
    index_max_value = (df_results_max['dollar_price'].idxmax())
    row = df_results_max.loc[index_max_value]
    results = f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"
    return results


if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(year, country_code)
    print(result_a)
    result_b = get_big_mac_price_by_country(country_code)
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(year)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(year)
    print(result_d)
