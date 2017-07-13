import numpy as np
from datetime import datetime

def detestr2num(s):
	return datetime.strptime(s,"%Y-%m-%d").date().weekday()


dates, opens, high, low, close = np.loadtxt('data.csv', delimiter=',',usecols=(0,1,2,3,4),converters={0:detestr2num},unpack=True)
close = close[:16]
dates = dates[:16]

#get first Monday
first_monday = np.ravel(np.where(dates == 0))[0]
print "The first Monday index is",first_monday

#get last Friday
last_friday = np.ravel(np.where(dates == 4))[-1]
print "The last Friday index is ", last_friday

weeks_indices = np.arange(first_monday, last_friday)
print "Weeks indices initial ",weeks_indices

weeks_indices = np.split(weeks_indices, 3)
print "Weeks indices after split ",weeks_indices

def summarize(a, o, h, l, c):
	monday_open = o[a[0]]
	week_high = np.max(np.take(h, a))
	week_low = np.min(np.take(l, a))
	friday_close = c[a[-1]]

	return("000001", monday_open, week_high, week_low, friday_close)

weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, opens, high, low, close)
print "Week summary ", weeksummary

#np.savetxt("weeksummary.csv", weeksummary, delimiter=',', fmt = "%s")