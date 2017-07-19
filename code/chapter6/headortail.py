import numpy as np
from matplotlib.pyplot import plot, show

cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size = len(cash))

print "outcome part: ", outcome[:50]

for i in range(1, len(cash)):
    if outcome[i] < 5:
		cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
		cash[i] = cash[i - 1] + 1
    else:
		raise AssertionError("Unexpected outcome " + outcome)
print outcome.min(), outcome.max()
print "cash head part: ",cash[:50]
print "cash tail part: ",cash[-50:]


plot(np.arange(len(cash)), cash)
show()
