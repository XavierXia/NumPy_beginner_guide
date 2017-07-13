import numpy as np

c = np.loadtxt('data.csv', delimiter=',',usecols=(4,),unpack=True)
print "median = ", np.median(c)

sorted_close = np.msort(c)
print "sorted = ", sorted_close
N = len(c)
print "N = ", N
print "middle = ", (sorted_close[N/2] + sorted_close[(N -1)/2])/2

print "variance = ", np.var(c)
print "variance from definition = ",np.mean((c - c.mean())**2)