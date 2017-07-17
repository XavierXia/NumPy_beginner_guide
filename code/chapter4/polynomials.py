# -*- coding: utf-8 -*-

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

#一个三次多项式去拟合两只股票收盘价的差价
zx = np.loadtxt('datazx.csv', delimiter=',', usecols=(4,), unpack=True)
zx = zx[:50]

ht = np.loadtxt('dataht.csv', delimiter=',', usecols=(4,), unpack=True) 
ht = ht[:50]

t = np.arange(len(zx))
poly = np.polyfit(t, zx - ht, int(sys.argv[1]))
#多项式的系数
print "Polynomial fit", poly

print "Next value", np.polyval(poly, t[-1] + 1)
#拟合的多项式函数什么时候到达0值,也就是函数的极值
print "Roots", np.roots(poly)

#对多项式函数求导
der = np.polyder(poly)

#二项式函数的导函数(仍然是一个多项式函数)的系数
print "Derivative", der

#找出原多项式函数的极值点,即导数的根
print "Extremas", np.roots(der)

#使用polyval计算多项式函数的值
vals = np.polyval(poly, t)
print np.argmax(vals)
print np.argmin(vals)

plot(t, zx - ht)
plot(t, vals)
show()