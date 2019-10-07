import pandas as pd

sym = "AAPL"  # This is not case-sensitive
token = "pk_ea365ed7ba2a49deb6404cd426913ac7"
df_temp = pd.read_json('https://cloud.iexapis.com/stable/stock/'+sym+'/chart/1y?token='+token+'')

df_temp.set_index('date',inplace=True)
stock_hist = df_temp['close']
stock_hist.tail(5)
