# -*- coding: utf-8 -*-

from matplotlib.finance import quotes_historical_yahoo
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def datestr2num(s):
	return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

#获取股票数据
quotes = np.loadtxt('../chapter3/data.csv',delimiter=',',usecols=(0,1,2,3,4),converters={0:datestr2num},unpack=False)
print "quotes: ", quotes[:5]
quotes = quotes[::-1]

quotes = np.array(quotes)
close = quotes.T[4]
print "close len: ",len(close)
plt.hist(close, np.sqrt(len(close)))
plt.show()