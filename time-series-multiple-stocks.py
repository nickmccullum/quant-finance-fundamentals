import pandas as pd

arrayOfSymbols = ["AAPL","FB","GOOG"]
sym = "AAPL"  # This is not case-sensitive
token = "pk_ea365ed7ba2a49deb6404cd426913ac7"
historicalStockPrices = pd.DataFrame()

for x in arrayOfSymbols:
    historicalStockPrices[x] = pd.read_json('https://cloud.iexapis.com/stable/stock/'+x+'/chart/1y?token='+token+'')["close"]   

historicalStockPrices.head(5)    
historicalStockPrices.head(5)
