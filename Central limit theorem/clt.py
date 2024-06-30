import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

fig = plt.figure('Central limit theorem')
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# number of datapoints in each sample
datapoints = 2000
# number of samples
number_of_samples = 4000

# mean = shape*scale, std dev = sqrt(shape) * scale
shape = 5
scale = 10

sample = np.array([np.random.gamma(shape, scale, datapoints) for i in range(number_of_samples)])
samplemeans = np.array([dataset.mean() for dataset in sample])

# GRAPH 1
# histogram of values in first sample
n1, bins1, patches1 = ax1.hist(sample[0], np.arange(0,max(sample[0]),1), density=True)
# line of best fit (gamma), then values on corresponding pdf values from that fit line
alpha, loc, beta = scipy.stats.gamma.fit(sample[0])
gammaapprox = scipy.stats.gamma.pdf(np.arange(0,max(sample[0]),0.5), alpha, loc, beta)
# plot fit line
ax1.plot(np.arange(0,max(sample[0]),0.5), gammaapprox, color='k', linewidth=2)
# plot vertical line at sample mean
ax1.vlines(sample[0].mean(), 0, scipy.stats.gamma.pdf(sample[0].mean(), alpha, loc, beta), color='r',linewidth=0.8)
# labels
ax1.text(sample[0].mean() + sample[0].std(), scipy.stats.gamma.pdf(sample[0].mean(), alpha, loc, beta),
         f'$\\mu = {np.round(sample[0].mean(), 2)}, \\sigma = {np.round(sample[0].std(), 2)}$')
ax1.set_title('Sample 1 of gamma variables')
ax1.set_ylabel('Frequency density')
ax1.set_xlabel('x')
ax1.grid(True)


# GRAPH 2
# histogram of sample means
n2, bins2, patches2 = ax2.hist(samplemeans, np.linspace(min(samplemeans),max(samplemeans),200), density=True)
# fit line for sample means (normal), then get 200 values using fit line in given range (min to max)
mu, sigma = scipy.stats.norm.fit(samplemeans)
normalapprox = scipy.stats.norm.pdf(np.linspace(min(samplemeans), max(samplemeans), 200),mu,sigma)
# plot fit line
ax2.plot(np.linspace(min(samplemeans), max(samplemeans), 200), normalapprox, color='k', linewidth=2)
# labels
ax2.text(mu + sigma, scipy.stats.norm.pdf(mu, mu, sigma),
         f'$\\mu = {np.round(samplemeans.mean(),2)}, \\sigma = {np.round(samplemeans.std(),2)}$')
ax2.set_title(f'Sample means of {str(datapoints)} gamma samples\n(normally distributed by central limit theorem)')
ax2.set_ylabel('Frequency density')
ax2.set_xlabel('Sample mean')
ax2.grid(True)

plt.suptitle('Central limit theorem', fontsize=20)
plt.tight_layout()
plt.show()