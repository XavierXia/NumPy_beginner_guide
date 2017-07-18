# -*- coding: utf-8 -*-
import numpy as np
import sys

o, h, l, c = np.loadtxt('datazx.csv', delimiter=',', usecols=(1, 2, 3, 4), unpack=True)
o = o[-50:]
h = h[-50:]
l = l[-50:]
c = c[-50:]
#print "o, h, l, c", o,h,l,c

def calc_profit(opens, high, low, close):
	#在开盘时买入
	buy = opens * float(sys.argv[1])

	#当日股价区间
	if low < buy < high:
		return (close - buy)/buy
	else:
		return 0

#相当于Python中的map函数
func = np.vectorize(calc_profit)
profits = func(o, h, l, c)
print "Profits", profits

real_trades = profits[profits != 0]
print "real_trades ", real_trades
print "Number of trades", len(real_trades), round(100.0 * len(real_trades)/len(c), 2), "%"
print "Average profit/loss %", round(np.mean(real_trades) * 100, 2)

winning_trades = profits[profits > 0]
print "Number of winning trades", len(winning_trades), round(100.0 *len(winning_trades)/len(c), 2), "%"
print "Average profit %", round(np.mean(winning_trades) * 100, 2)

losing_trades = profits[profits < 0]
print "Number of losing trades", len(losing_trades), round(100.0 *len(losing_trades)/len(c), 2), "%"
print "Average loss %", round(np.mean(losing_trades) * 100, 2)
