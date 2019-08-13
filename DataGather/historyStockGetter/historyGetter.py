import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas_datareader.data as web
import pandas as pd
symbol = []


def gettickername():

    with open('fortune5') as f:
        for line in f:
            symbol.append(line.strip())
    f.close()
    return symbol


def getstockdata(reload_sp500=False, symbol=symbol):
    i = 1950
    if not os.path.exists('stockData_dfs'):
        os.makedirs('stockData_dfs')
    start = dt.datetime(i, 1, 1)
    end = dt.datetime.today()
    for symbol in symbol:
        print(symbol)
        i = 1950
        while i < 2019:
            start = dt.datetime(i, 1, 1)
            i = i + 1
            if not os.path.exists('stockData_dfs/{}.csv'.format(symbol)):
                try:
                    df = web.DataReader(symbol, 'yahoo', start, end)
                    df.to_csv('stockData_dfs/{}.csv'.format(symbol))
                    df = pd.read_csv(symbol, parse_dates=True, index_col=0)
                    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
                    print(df.head())
                except:
                    break
                    break
gettickername()
getstockdata()