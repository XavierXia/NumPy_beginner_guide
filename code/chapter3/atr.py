import numpy as np
import sys

h,l,c = np.loadtxt('data.csv', delimiter=',',usecols=(2,3,4), unpack=True)

N = int(sys.argv[1])
h = h[-N:]
l = l[-N:]

print "len(h) ", len(h), "len(l) ", len(l)
print "Close ", c
previousclose = c[-N-1:-1]
print "previousclose: ", previousclose

print "len(previousclose)",len(previousclose)
print "Previous close", previousclose
truerange = np.maximum(h - l, h - previousclose, previousclose - l)

print "True range", truerange

atr = np.zeros(N)

atr[0] = np.mean(truerange)

for i in range(1,N):
	atr[i] = (N - 1)*atr[i-1] + truerange[i]
	atr[i] /= N

print "ATR ", atr