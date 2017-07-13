import numpy as np

c = np.loadtxt('data.csv', delimiter=',',usecols=(4,),unpack=True)

returns = np.diff(c)/c[:-1]
print "Standard deviation =", np.std(returns)
logreturns = np.diff(np.log(c))
#print "logreturns =",logreturns

posretindices = np.where(returns > 0)
print "Indics with positive returns", posretindices

annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility/np.sqrt(1./252.)
print annual_volatility

print "monthly volatility", annual_volatility*np.sqrt(1./12.)