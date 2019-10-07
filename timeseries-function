from iexfinance.stocks import Stock 
from datetime import datetime, timedelta 
import numpy as np 
from iexfinance.stocks import get_historical_data
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

plt.rcParams['figure.figsize'] = (20,8)

import seaborn as sns;
sns.set(font_scale = 1.5)
sns.set_style("whitegrid")

tickerSymbol = input("Ticker Symbol: ")
companyInfo = Stock(tickerSymbol)
stockPrice = companyInfo.get_price()

print("Current Stock Price: ",stockPrice)

print("View Historical Information for the Current Stock {}:".format(tickerSymbol))
sy, sm, sd = eval(input("input start date as yyyy,m,d: "))
ey, em, ed = eval(input("input end date as yyyy,m,d: "))

start = datetime(sy,sm,sd)
end = datetime(ey,em,ed)

historicalPrices = get_historical_date(tickerSymbol, start, end)

stockHistoricals = pd.DataFrame(historicalPrices).T 

startingDate = (sy*10000)+(sm*100)+sd
endingDate = (ey*10000)+(em*100)+ed

fileName = "HistoricalStockPrices_" + tickerSymbol + "_From_" + str(startingDate) + "_To_" + str(endingDate) + ".xlsx"

stockHistoricals.to_excel(fileName)
