"""Nasdaq Portfolio Generator

This script allows the user to generate a CSV file that contains each of the components
of the Nasdaq 100 index along with how much to invest in each stock.

This tool accepts a valid number as input and outputs a CSV file.

This script requires that `pandas`, `bs4` and `requests` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * soup - returns the BeautifulSoup parsed html source of the url
    * create_raw_df - returns a Pandas DataFrame of the raw Nasdaq data
    * create_output_df - returns a Pandas DataFrame of the dollar amount to put into each stock
    * main - the main function of the script
"""

import sys
import os
from bs4 import BeautifulSoup
import pandas as pd
import requests

def soup(url):
    """Returns the BeautifulSoup parsed html source of the inputted url

    Parameters
    ----------
    url : str
        The url that contins the Nasdaq information

    Returns
    -------
    bs4.BeautifulSoup
    """
    page = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    return BeautifulSoup(page.text, "html.parser")

def create_raw_df():
    """Generates a Pandas DataFrame of the raw Nasdaq data

    Parameters
    ----------
    None

    Returns
    -------
    pandas.DataFrame
    """
    url = "https://www.slickcharts.com/nasdaq100"
    nasdaq_soup = soup(url)
    td_list = nasdaq_soup.findAll("td")
    print("Successfully scraped data...")
    td_list = [val.text for val in td_list]
    td_list_2d = [td_list[i+1:i+7] for i in range(0,len(td_list), 7)] #selects columns 1-6 of table
    nasdaq_df = pd.DataFrame(td_list_2d, columns=["Company", "Ticker", "Weight", "Price", "Chg", "%Chg"])
    nasdaq_df["Price"] = [float(val.replace(',','')) for val in nasdaq_df["Price"]] #makes the price data numerical, strips commas
    nasdaq_df["Weight"] = nasdaq_df["Weight"].astype(float)
    return nasdaq_df

def create_output_df(df):
    """Generates a Pandas DataFrame of the dollar amount to put into each stock

    Parameters
    ----------
    pandas.DataFrame
        a DataFrame of the raw Nasdaq data

    Returns
    -------
    pandas.DataFrame
    """
    try:
        cash_available = float(sys.argv[1])
    except:
        print("Please enter a valid number.")
        sys.exit()
    equal_weighted = (cash_available / df["Price"].sum()) * df["Price"]
    cap_weighted = (cash_available/100) * df["Weight"]
    blended_weights = (equal_weighted + cap_weighted) / 2  #this averages the market cap weighted and equal weighted columns
    cols = ["Ticker", "Equal Weighted", "Cap Weighted", "$ Amount to Buy"]
    zipped_cols = zip(df["Ticker"], equal_weighted, cap_weighted, blended_weights)
    export_df = pd.DataFrame(zipped_cols, columns=cols).round(2)
    return export_df

def main():
    nasdaq_df = create_raw_df()
    export_df = create_output_df(nasdaq_df)
    export_df.to_csv("amount_to_buy.csv")
    print("CSV complete!")
    os.startfile("amount_to_buy.csv")

if __name__ == "__main__":
    main()
