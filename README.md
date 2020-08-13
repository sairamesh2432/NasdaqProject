## Nasdaq Portfolio Generator

This script allows the user to generate a CSV file that contains each of the components
of the Nasdaq 100 index along with how much to invest in each stock.

## Motivation
I started this project after finding out that there were no low-cost (below 0.1% expense ratio) index funds that tracked the Nasdaq-100. Luckily, you can craft your own index fund with the power of fractional shares, so I started this project to help me automate that process.

## How to use?
This is a command line interface. Simply input as an argument the amount of cash available to invest (in USD) when running the script in the terminal. 

python nasdaq.py 224

## Dependencies
This script requires the pandas, bs4, and requests modules to be installed.


## Credits

All stock price data comes from https://www.slickcharts.com/nasdaq100

