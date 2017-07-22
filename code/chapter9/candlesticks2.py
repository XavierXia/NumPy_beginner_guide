# -*- coding: utf-8 -*-

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import sys
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.finance as f

def datestr2num(s):
	return datetime.strptime(s, "%Y-%m-%d").date().weekday()

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

#获取股票数据
dates,opens,close,high,low = np.loadtxt('../chapter/data.csv',delimiter=',',usecols=(1,4),converters={0:datestr2num},unpack=True)

#绘图组件的顶层容器
fig = plt.figure()
#增加一个子图
ax = fig.add_subplot(111)

#将x轴上的主定位器设置为 月和日 定位器
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

#绘制K线图
f.candlestick2_ohlc(ax, opens,close,high,low)
#将x轴上的标签格式化日期
fig.autofmt_xdate()
plt.show()