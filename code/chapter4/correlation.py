# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

#股票收益率
zx = np.loadtxt('datazx.csv', delimiter=',', usecols=(4,), unpack=True)[::-1]
zx = zx[:20]
zx_returns = np.diff(zx)/zx[:-1]

ht = np.loadtxt('dataht.csv', delimiter=',', usecols=(4,), unpack=True)[::-1]
ht = ht[:20]
ht_returns = np.diff(ht)/ht[:-1]

#计算股票收益率的协方差矩阵
covariance = np.cov(zx_returns, ht_returns)
print "covariance ",covariance

#查看对角线上的元素
print "Covariance diagonal", covariance.diagonal()
#计算矩阵的迹，即对角线上元素之和
print "Covariance trace", covariance.trace()

#计算向量a和b的相关系数,用相关系数来度量这两只股票的相关程度
print covariance/ (zx_returns.std() * ht_returns.std())
print "Correlation coefficient", np.corrcoef(zx_returns, ht_returns)

#如果它们的差值偏离了平均差值2 倍于标准差的距离，则认为这两只股票走势不同步。
#若判断为不同步，我们可以进行股票交易
difference = zx - ht
avg = np.mean(difference)
dev = np.std(difference)
print "Out of sync", np.abs(difference[-1] - avg) > 2 * dev

t = np.arange(len(zx_returns))
plot(t, zx_returns, lw=1)
plot(t, ht_returns, lw=2)
show()