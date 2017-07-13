# -*- coding: utf-8 -*-

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

'''
	该处有几个数学概念,如
	1.标准差,公式:sqrt(((x1-x)^2 +(x2-x)^2 +......(xn-x)^2)/n)
	2.python list的运用
		print str[0:3] #截取第一位到第三位的字符
		print str[:] #截取字符串的全部字符
		print str[6:] #截取第七个字符到结尾
		print str[:-3] #截取从头开始到倒数第三个字符之前
		print str[2] #截取第三个字符
		print str[-1] #截取倒数第一个字符
		print str[::-1] #创造一个与原字符串顺序相反的字符串
		print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
		print str[-3:] #截取倒数第三位到结尾
		print str[:-5:-3] #逆序截取
'''

#N = int(sys.argv[1])
N = 100

weights = np.ones(N)/N
#print "Weights ",weights

c = np.loadtxt('data.csv', delimiter=',', usecols=(4,), unpack=True)[::-1]
c = c[:400]
#print "c :",c

'''
0 1 2 3 ... 99,   100,101,...,200,201,...,  300,301,...,400
'''
sma = np.convolve(weights, c)[N-1:-N+1]
deviation = []
C = len(c)
print "C: ",C
print "sma: ", sma, len(sma)

for i in range(N-1,C):
	if i + N < C:
		dev = c[i:i + N]
		#print "dev: ",dev
	else:
		dev = c[-N:]
		#print "dev2: ",dev

	#下面为标准差的计算公式
	averages = np.zeros(N)
	averages.fill(sma[i-N-1])
	dev = dev - averages
	dev = dev ** 2
	dev = np.sqrt(np.mean(dev))
	deviation.append(dev)

'''
中轨:简单移动平均线
上轨:比简单移动平均线高两倍标准差的距离
下轨:比简单移动平均线低两倍标准差的距离
'''
deviation = 2 * np.array(deviation)
print len(deviation), len(sma)
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N-1:]
between_bands = np.where((c_slice < upperBB)&(c_slice > lowerBB))

print lowerBB[between_bands]
print c[between_bands]
print upperBB[between_bands]
between_bands = len(np.ravel(between_bands))
print "Ratio between bands", float(between_bands)/len(c_slice)

t = np.arange(N-1,C)
plot(t, c_slice, lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()