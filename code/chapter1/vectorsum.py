#!/usr/bin/env/python

import sys
from datetime import datetime
import numpy as np

'''
		python vectorsum.py n

		1.
		TDX-HB:python_data hebo$ python vectorsum.py 1000
		the last 2 elements of the sum [995007996, 998001000]
		pythonsum elapsed time in microseconds 733
		the last 2 elements of the sum [995007996 998001000]
		numpy elapsed time in microseconds 105

		2.
		TDX-HB:python_data hebo$ python vectorsum.py 2000
		the last 2 elements of the sum [7980015996, 7992002000]
		pythonsum elapsed time in microseconds 1762
		the last 2 elements of the sum [7980015996 7992002000]
		numpy elapsed time in microseconds 159

		3.
		TDX-HB:python_data hebo$ python vectorsum.py 3000
		the last 2 elements of the sum [26955023996, 26982003000]
		pythonsum elapsed time in microseconds 2246
		the last 2 elements of the sum [26955023996 26982003000]
		numpy elapsed time in microseconds 220
'''

def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b

	return c

def pythonsum(n):
	a = range(n)
	b = range(n)
	c = []

	for i in range(len(a)):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i] + b[i])

	return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print "the last 2 elements of the sum", c[-2:]
print "pythonsum elapsed time in microseconds", delta.microseconds

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print "the last 2 elements of the sum", c[-2:]
print "numpy elapsed time in microseconds", delta.microseconds