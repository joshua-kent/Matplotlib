import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

plt.figure()
# produces a set of 2000 datapoints from a chi square distribution, 10 degrees of freedom
x = np.random.chisquare(10, 2000)
x1 = np.arange(40)
# creates a histogram (density=True means frequency density rather than simple density), with bins from 0 to 30, size 0.5
n, bins, patches = plt.hist(x, np.arange(0, 30, 0.5), density=True)

# fits the data in 'x' to a chi squared distribution, defines parameters
shape,loc,scale = scipy.stats.chi2.fit(x)
# produces y values at each value in each bin, for the fitted chi square distribution
y_bestfit = scipy.stats.chi2.pdf(bins, shape, loc, scale)
# plots line of best fit (according to a chi squared distribution)
plt.plot(bins, y_bestfit, 'k')
plt.xlim(left=0, right=30)
plt.ylim(bottom=0)
plt.ylabel('Frequency density')
plt.title('Chi squared sample')

plt.grid(True)
plt.show()