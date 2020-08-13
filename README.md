## Nasdaq Portfolio Generator

This script allows the user to generate a CSV file that contains each of the components
of the Nasdaq 100 index along with how much to invest in each stock.

## Motivation
I started this project after finding out that there were no low-cost (below 0.1% expense ratio) index funds that tracked the Nasdaq 100 index. Luckily, it's possible to craft your own index fund with the power of fractional shares, so I started this project to help me automate that process.

The dollar values apportioned to each stock are based on an average between **equal-weighting** and **cap-weighting** methodologies. Under an equal-weighting system, each stock in the index would receive an equal amount of shares, while under a cap-weighted system, larger companies recieve higher weight. 

Both systems have their own set of advantages and disadvantages, so I decided to attempt a middle ground and average the two. 

## How to use?
This script takes arguments from the command line. Simply input as an argument the amount of cash available to invest (in USD) when running the script in the terminal. 

**Example:**
python nasdaq.py 224

With this command, the outputted CSV file will distribute $224 between the 100 component stocks.

## Dependencies
This script requires the pandas, bs4, and requests modules to be installed.


## Credits

All stock price data comes from https://www.slickcharts.com/nasdaq100

