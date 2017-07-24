# -*- coding: utf-8 -*-

from datetime import datetime
import numpy as np
from scipy import stats
from statsmodels.stats.stattools import jarque_bera
import matplotlib.pyplot as plt

'''
样本数据的对数收益率
'''
def datestr2num(s):
    return datetime.strptime(s,"%Y-%m-%d").date().toordinal()

def get_close(symbol):
	#获取股票数据
	quotes = np.loadtxt(symbol,delimiter=',',converters={0:datestr2num},unpack=False)
	print "quotes: ", quotes[:5]
	quotes = quotes[::-1]
	quotes = np.array(quotes)
	return quotes.T[4]

zx = np.diff(np.log(get_close('../chapter4/datazx.csv')))
zx = zx[:550]
ht = np.diff(np.log(get_close('../chapter4/dataht.csv')))
ht = ht[:550]

print "Means comparison", stats.ttest_ind(zx, ht)
print "Kolmogorov smirnov test", stats.ks_2samp(zx, ht)
print "Jarque Bera test", jarque_bera(zx - ht)[1]

plt.hist(zx, histtype="step", lw=1, label="zx")
plt.hist(ht, histtype="step", lw=2, label="ht")
plt.hist(zx - ht, histtype="step", lw=3, label="Delta")

plt.legend()
plt.show()