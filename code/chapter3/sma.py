import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

c = np.loadtxt('data.csv', delimiter=',', usecols=(4,), unpack=True)[::-1]
print "c: ", c

N = int(sys.argv[1])
#N = len(c)

weights = np.ones(N) / N
print "weights ", weights[0:20]

sma = np.convolve(weights, c)[N-1:-N+1]

t = np.arange(N-1,len(c))

plot(t,c[N-1:],lw=1.0)
plot(t,sma,lw=2.0)
show()
