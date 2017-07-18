# -*- coding: utf-8 -*-

import numpy as np

c, v = np.loadtxt('datazx.csv', delimiter=',', usecols=(4, 5), unpack=True)[::-1]
c = c[:50]
v = v[:50]

change = np.diff(c)
print "Change", change

#返回数组中每个元素的正负符号，数组元素为负时返回-1，为正时返回1，否则返回0
signs = np.sign(change)
print "Signs", signs

#获取数组元素的正负
pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1])
print "Pieces", pieces

print "Arrays equal?", np.array_equal(signs, pieces)
print "On balance volume", v[1:] * signs