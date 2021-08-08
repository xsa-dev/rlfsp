import sys
import yfinance as yf
import pandas as pd

if len(sys.argv) != 3:
	print("Usage: python load.py [stock] [timeseries](1mo,1y)")	
	exit()

print(f'Stock: {sys.argv[1]}')
print(f'Period: {sys.argv[2]}')
d = yf.download(sys.argv[1], period=sys.argv[2])
print(d)
d.to_csv(f'data/{sys.argv[1]}.csv', index=False)
print('loaded.')