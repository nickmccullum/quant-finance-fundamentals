import pandas as pd
import numpy as np

#import the stock tickers as an array of nested arrays

doubleArrayOfTickers = np.array(pd.read_csv("stock_tickers.csv",header=None))
arrayOfTickers = []

i=0

#loop through the arrays of arrays and append them into a new, cleaned array

while i < len(doubleArrayOfTickers):
    arrayOfTickers.append(doubleArrayOfTickers[i][0])
    i += 1

#add in your IEX Cloud token and create an empty DataFrame
    
token = "pk_ea365ed7ba2a49deb6404cd426913ac7"
historicalStockPrices = pd.DataFrame()

#add price data for each security into the empty historicalStockPrices array, then index the date and save as .csv

for x in arrayOfTickers:
    historicalStockPrices[x] = pd.read_json('https://cloud.iexapis.com/stable/stock/'+x+'/chart/1y?token='+token+'')["close"]     

historicalStockPrices["date"] = pd.read_json('https://cloud.iexapis.com/stable/stock/AAPL/chart/1y?token='+token+'')["date"]
historicalStockPrices.set_index('date',inplace=True)

historicalStockPrices.to_csv('historicalStockPrices - 1 Year.csv')

#create empty array for daily historical returns

historicalStockReturns = pd.DataFrame()

#add daily return data for each security into the empty historicalStockReturns array, then save as .csv

for y in arrayOfTickers:
    historicalStockReturns[y] = (historicalStockPrices[y] / historicalStockPrices[y].shift(1) ) - 1      

historicalStockReturns.to_csv('historicalDailyStockReturns - 1 Year.csv')

#calculate cumulative return and save to .csv

cumulativeHistoricalStockReturns = ((historicalStockReturns+1).cumprod()-1).iloc[-1].to_frame()
cumulativeHistoricalStockReturns.to_csv('cumulativeStockReturns - 1 Year.csv')
