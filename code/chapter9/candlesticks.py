# -*- coding: utf-8 -*-

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.finance import candlestick
import sys
from datetime import date
import matplotlib.pyplot as plt

'''
被墙了,获取不到数据,我会使用上几章用过的数据来测试,见 candlesticks2.py
'''

today = date.today()
print "today: ", today
start = (today.year - 1, today.month, today.day)
print "start: ", start

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

symbol = '^GSPC'
#if len(sys.argv) == 2:
#	symbol = sys.argv[1]

#获取股票数据
quotes = quotes_historical_yahoo(symbol, start, today)
#quotes = quotes_historical_yahoo_ochl(symbol, start, today,asobject=True, adjusted=True)
print "quotes: ",quotes[:2]

#绘图组件的顶层容器
fig = plt.figure()
#增加一个子图
ax = fig.add_subplot(111)

#将x轴上的主定位器设置为 月和日 定位器
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

#绘制K线图
#candlestick_ochl(ax, quotes)
candlestick(ax, quotes)
#将x轴上的标签格式化日期
fig.autofmt_xdate()
plt.show()