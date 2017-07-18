# -*- coding: utf-8 -*-
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# N一般取8
# N = int(sys.argv[1])
N = 8
weights = np.hanning(N)
print "Weights", weights

zx = np.loadtxt('datazx.csv', delimiter=',', usecols=(4,), unpack=True) 
zx = zx[-50:]
zx_returns = np.diff(zx) / zx[ : -1]
smooth_zx = np.convolve(weights/weights.sum(), zx_returns)[N-1: -N+1]

ht = np.loadtxt('dataht.csv', delimiter=',', usecols=(4,), unpack=True) 
ht = ht[-50:]
ht_returns = np.diff(ht) / ht[ : -1]
smooth_ht = np.convolve(weights/weights.sum(), ht_returns)[N-1: -N+1]

#使用多项式拟合平滑后的数据
#K = int(sys.argv[1])
K = 3
t = np.arange(N - 1, len(zx_returns))
poly_zx = np.polyfit(t, smooth_zx, K)
poly_ht = np.polyfit(t, smooth_ht, K)

poly_sub = np.polysub(poly_zx, poly_ht)
xpoints = np.roots(poly_sub)
print "Intersection points", xpoints

reals = np.isreal(xpoints)
print "Real number?", reals

xpoints = np.select([reals], [xpoints])
xpoints = xpoints.real
print "Real intersection points", xpoints
print "Sans 0s", np.trim_zeros(xpoints)

plot(t, zx_returns[N-1:], lw=1.0)
plot(t, smooth_zx, lw=2.0)
plot(t, ht_returns[N-1:], lw=1.0)
plot(t, smooth_ht, lw=2.0)
show()