# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

t = np.linspace(-np.pi, np.pi, 201)

#k = 100
k = np.arange(1, float(sys.argv[1]))
k = 2 * k - 1
print "k ", k

f = np.zeros_like(t)

print "t ", t
print "f ", f

for i in range(len(t)):
	#使用NumPy函数摆脱循环，并确保你的代 码性能因此而得到提升
	f[i] = np.sum(np.sin(k * t[i])/k)

f = (4 / np.pi) * f
plot(t, f)
show()