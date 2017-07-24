# -*- coding: utf-8 -*-

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def datestr2num(s):
    return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

#获取股票数据
quotes = np.loadtxt('../chapter3/data.csv',delimiter=',',converters={0:datestr2num},unpack=False)
print "quotes: ", quotes[:5]
quotes = quotes[::-1]

quotes = np.array(quotes)
close = quotes.T[4]
volume = quotes.T[5]

ret = np.diff(close)/close[:-1]
volchange = np.diff(volume)/volume[:-1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(ret, volchange, c=ret * 100, s=volchange * 100, alpha=0.5)
ax.set_title('Close and volume returns')
ax.grid(True)
plt.show()