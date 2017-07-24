# -*- coding: utf-8 -*-

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator

def datestr2num(s):
    return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

#获取股票数据
quotes = np.loadtxt('../chapter3/data.csv',delimiter=',',converters={0:datestr2num},unpack=False)
print "quotes: ", quotes[:5]
quotes = quotes[::-1]

quotes = np.array(quotes)
dates = quotes.T[0]
close = quotes.T[4]

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(dates, close)

plt.fill_between(dates, close.min(), close, where=close>close.mean(), facecolor="green", alpha=0.4)
plt.fill_between(dates, close.min(), close, where=close<close.mean(), facecolor="red", alpha=0.4)

ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

ax.grid(True)
fig.autofmt_xdate()
plt.show()