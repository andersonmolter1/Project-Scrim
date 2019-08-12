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

    if not os.path.exists('stockData_dfs'):
        os.makedirs('stockData_dfs')
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime.today()
    i = 2000
    for symbol in symbol:
        if not os.path.exists('stockData_dfs/{}.csv'.format(symbol)):
            try:
                df = web.DataReader(symbol, 'yahoo', start, end)
                df.to_csv('stockData_dfs/{}.csv'.format(symbol))
            except:
                print(symbol)
                continue
        else:
            print('Already have {}'.format(symbol))


gettickername()
getstockdata()