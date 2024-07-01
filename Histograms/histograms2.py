import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats
import math

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

df=12
datapoints = 2000

data = np.random.chisquare(df, datapoints)

# Probability density function
sns.histplot(x=data, stat='density', kde=True, ax=ax1, binwidth=0.5)
ax1.set_title('pdf')

shape, loc, scale = scipy.stats.chi2.fit(data)
ideal = scipy.stats.chi2.pdf(np.linspace(data.min(), data.max(), datapoints), shape, loc, scale)
ax1.plot(np.linspace(data.min(), data.max(), datapoints), ideal, 'k--')

# Cumulative distribution function
sns.histplot(x=data, stat='density', cumulative=True, kde=True, ax=ax2, binwidth=0.5)
ax2.set_title('cdf')

plt.tight_layout()
plt.show()