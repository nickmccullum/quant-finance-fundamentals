import pandas as pd
import numpy as np

doubleArrayOfTickers = np.array(pd.read_csv("stock_tickers.csv"))

arrayOfTickers = []

i=0

while i < len(doubleArrayOfTickers):
    arrayOfTickers.append(doubleArrayOfTickers[i][0])
    i += 1

token = "pk_ea365ed7ba2a49deb6404cd426913ac7"
historicalStockPrices = pd.DataFrame()

for x in arrayOfTickers:
    historicalStockPrices[x] = pd.read_json('https://cloud.iexapis.com/stable/stock/'+x+'/chart/1y?token='+token+'')["close"]     

historicalStockPrices["date"] = pd.read_json('https://cloud.iexapis.com/stable/stock/AAPL/chart/1y?token='+token+'')["date"]
historicalStockPrices.set_index('date',inplace=True)
