# -*- coding: utf-8 -*-

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
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
dates = quotes.T[0]
volume = quotes.T[5]

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = plt.figure()
ax = fig.add_subplot(111)

plt.semilogy(dates, volume)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

fig.autofmt_xdate()
plt.show()