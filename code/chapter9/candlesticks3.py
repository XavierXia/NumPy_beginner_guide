# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import sys
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick

'''
调了大半天，终于成功了，主要原因还是在系统调用的matplotlib.finance代码版本不兼容造成的，
有的系统中 使用的finance.py中有candlestick2函数，而有的没有，只有更新后的candlestick2_ochl函数，
所以总会出现没有该函数的提示。
确定该问题的过程如下：
1. 查看系统中使用matplotlib是哪个版本的：
>>> python -c "import matplotlib; print matplotlib.__file__"
/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/__init__.pyc
2. 进入/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib中找到finance.py
3. 查看finance.py中使用了candlestick2还是candlestick2_ochl。
4. 调用存在的函数即可。

现在显示出来的效果也是差强人意，后面会对此优化，效果要达到实盘效果。
'''

def datestr2num(s):
	return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

#获取股票数据
data = np.loadtxt('../chapter3/data.csv',delimiter=',',usecols=(0,1,2,3,4),converters={0:datestr2num},unpack=False)
print "data: ", data[:5]
data = data[::-1]

#绘图组件的顶层容器
fig = plt.figure()
#增加一个子图
ax = fig.add_subplot(111)

#将x轴上的主定位器设置为 月和日 定位器
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)

#绘制K线图
candlestick(ax,data,width=1, colorup='r', colordown='b', alpha=1.0)

#将x轴上的标签格式化日期
fig.autofmt_xdate()
plt.show()
