import pandas as pd
import numpy as np

doubleArrayOfTickers = np.array(pd.read_csv("stock_tickers.csv"))

arrayOfTickers = []

i=0

while i < len(doubleArrayOfTickers):
    arrayOfTickers.append(doubleArrayOfTickers[i][0])
    i += 1

print(arrayOfTickers)
