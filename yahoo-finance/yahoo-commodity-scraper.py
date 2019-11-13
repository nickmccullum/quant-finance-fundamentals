import requests from bs4 
import BeautifulSoup import csv 
import pandas as pd 

prices=[]
names=[]
changes=[]
percentChanges=[]
marketCaps=[]
marketTimes=[]
totalVolumes=[]
openInterests=[]
 
CryptoCurrenciesUrl = "https://in.finance.yahoo.com/commodities"
r= requests.get(CryptoCurrenciesUrl)
data=r.text
soup=BeautifulSoup(data)
 
counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
         for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for time in srow.find_all('td', attrs={'class':'data-col3'}):
            marketTimes.append(time.text)
         for change in srow.find_all('td', attrs={'class':'data-col4'}):
            changes.append(change.text)
         for percentChange in srow.find_all('td', attrs={'class':'data-col5'}):
            percentChanges.append(percentChange.text)
         for volume in srow.find_all('td', attrs={'class':'data-col6'}):
            totalVolumes.append(volume.text)
         for openInterest in srow.find_all('td', attrs={'class':'data-col7'}):
            openInterests.append(openInterest.text)

pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Time": marketTimes,'Open Interest': openInterests ,"Volume": totalVolumes})
