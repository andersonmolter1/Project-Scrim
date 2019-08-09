import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
import time
import datetime
from datetime import date
import pandas_datareader.data as web
symbol = []
with open('/Users/Anderson Molter/Down
loads/F500List.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close

start = datetime.date.today()
end = datetime.date.today()

i=0
while i<len(symbol):
    try:
        f = web.DataReader(symbol[i], 'yahoo', start, end)
        f.insert(0,'Symbol',symbol[i])
        f = f.drop(['Adj Close'], axis=1)
        print (f)
    except :
        print("No information for ticker:" )
        print (symbol[i])
        continue
    i=i+1


