from pandas import Series, DataFrame
import numpy as py
import pandas as pd
from pandas_datareader import data, wb
import fix_yahoo_finance as yf
yf.pdr_override()

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = data.get_data_yahoo(ticker, '2010-01-01', '2010-02-02')

print(all_data[ticker])


pricesDict = {key: data['Adj Close']
                    for key, data in all_data.items()}
price = DataFrame(pricesDict)

print(price)

volumeDict = {key: data['Volume']
                        for key, data in all_data.items()}
volume = DataFrame(volumeDict)

print(volume)

returns = price.pct_change()
print(returns.tail())

print(returns.MSFT.corr(returns.IBM))

print(returns.MSFT.cov(returns.IBM))

print(returns.corr())

print(returns.cov())