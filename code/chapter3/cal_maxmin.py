import numpy as np

h,l = np.loadtxt('data.csv',delimiter=',',usecols=(2,3),unpack=True)
print "highest = ",np.max(h)
print "lowest = ",np.min(l)

print "Spread high price", np.ptp(h)
print "Spread low price", np.ptp(l)