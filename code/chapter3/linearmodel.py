# -*- coding: utf-8 -*-

import numpy as np
import sys

'''
最小二乘法
'''

N = int(sys.argv[1])

c = np.loadtxt('data.csv', delimiter=',', usecols=(4,), unpack=True)

b = c[-N:]
b = b[::-1]

print "b ", b

A = np.zeros((N, N), float)
print "Zeros N by N ", A

for i in range(N):
	A[i, ] = c[-N - 1 - i: -1 - i] #-11,-1  -12,-2

print "A ", A

(x, residuals, rank, s) = np.linalg.lstsq(A, b)
print x,residuals,rank,s
print np.dot(b, x)