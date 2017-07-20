# -*- coding: utf-8 -*-

import numpy as np
import datetime

def datestr2num(s):
	return datetime.datetime.strptime(s, "%Y-%m-%d").toordinal()

dates,closes = np.loadtxt('data.csv', delimiter=',', usecols=(0, 4), converters={0:datestr2num}, unpack=True)
print "dates: ", dates[:20]

#lexsort函数根据键值的字典序进行排序
indices = np.lexsort((dates, closes))

print "Indices", indices
print [" %s%s" % (datetime.date.fromordinal(int(dates[i])),closes[i]) for i in indices]