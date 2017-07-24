# -*- coding: utf-8 -*-

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

'''
感觉图例和注释代码 没有生效......后面优化一下.
'''

def datestr2num(s):
    return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

#获取股票数据
quotes = np.loadtxt('../chapter3/data.csv',delimiter=',',converters={0:datestr2num},unpack=False)
print "quotes: ", quotes[:5]
quotes = quotes[::-1]

dates = quotes.T[0]
close = quotes.T[4]
fig = plt.figure()
ax = fig.add_subplot(111)

emas = []
for i in range(9, 18, 3):
	weights = np.exp(np.linspace(-1., 0., i))
	weights /= weights.sum()
	ema = np.convolve(weights, close)[i-1:-i+1]
	idx = (i - 6)/3
	ax.plot(dates[i-1:], ema, lw=idx, label="EMA(%s)" % (i))
	data = np.column_stack((dates[i-1:], ema)) 
	emas.append(np.rec.fromrecords(data, names=["dates", "ema"]))

first = emas[0]["ema"].flatten()
second = emas[1]["ema"].flatten()
bools = np.abs(first[-len(second):] - second)/second < 0.0001
xpoints = np.compress(bools, emas[1])
print "xpoints part:", xpoints[:5]

for xpoint in xpoints:
	ax.annotate('x', xy=xpoint, textcoords='offset points',xytext=(-50, 30),arrowprops=dict(arrowstyle="->"))

leg = ax.legend(loc='best', fancybox=True)
leg.get_frame().set_alpha(0.5)

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
ax.plot(dates, close, lw=1.0, label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
plt.show()