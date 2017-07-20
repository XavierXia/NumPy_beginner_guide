# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.dates import datestr2num
from matplotlib.pyplot import plot, show, legend
import sys

closes = np.loadtxt('data.csv', delimiter=',', usecols=(4, ), converters={0:datestr2num}, unpack=True)[::-1]

#N = 30
N = int(sys.argv[1])
#调用blackman函数生成一个平滑窗并用它来平滑股价数据
window = np.blackman(N)
print "window part:", window[:20]
smoothed = np.convolve(window/window.sum(), closes, mode='same') 

plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()