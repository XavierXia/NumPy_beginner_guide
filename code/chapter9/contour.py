# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

'''
绘制简单的三维函数:
z = x ** 2 + y ** 2
'''

fig = plt.figure()
ax = fig.add_subplot(111)

u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
#色彩填充的等高线图
ax.contourf(x, y, z)
#非色彩填充的等高线图
#ax.contour(x, y, z)

plt.show()