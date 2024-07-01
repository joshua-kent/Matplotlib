import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


fig = plt.figure('Boxplots example')
ax1 = fig.add_subplot(131) # normal scatter
ax2 = fig.add_subplot(132) # poisson scatter
ax3 = fig.add_subplot(133) # boxplot
ax1_hist = ax1.inset_axes([0.6,0.8,0.35,0.15]) # produces a set of axes within another
ax2_hist = ax2.inset_axes([0.6,0.8,0.35,0.15])

datapoints=100
mean = 10
dev = 5
_lambda = 15

data_normal = {
    'x': np.arange(0, datapoints, 1),
    'y': np.random.normal(mean, dev, datapoints),
    'class': np.full(datapoints, 'Normal')
}
data_poisson = {
    'x': np.arange(0, datapoints, 1),
    'y': np.random.poisson(_lambda, datapoints),
    'class': np.full(datapoints, 'Poisson')
}

# ax1 (normal scatter)
ax1.scatter(x='x',y='y', data=data_normal, color='r', marker='x')
ax1.set_title(f'Normal data, $\\mu={mean}, \\sigma={dev}$')

# ax2 (poisson scatter)
ax2.scatter(x='x',y='y', data=data_poisson, marker='x')
ax2.set_title(f'Poisson data, $\\lambda={_lambda}$')
ax2.set_yticks(np.arange(data_poisson['y'].min()-1, data_poisson['y'].max()+1,1))

# ax3 (boxplots)
sns.boxplot(data=data_normal, x='class', y='y', ax=ax3, fill=False, color='r')
sns.boxplot(data=data_poisson, x='class', y='y', ax=ax3, fill=False)
ax3.set_title('Boxplots')

# ax1_hist (normal histogram)
sns.histplot(data=data_normal, x='y', ax=ax1_hist, stat='density', kde=True, binwidth=1)
ax1_hist.set_xlabel('')
ax1_hist.set_ylabel('')
ax1_hist.set_yticks([])
ax1_hist.set_xticks([mean])

# ax2_hist (poisson histogram)
sns.histplot(data=data_poisson, x='y', ax=ax2_hist, stat='density', kde=True, binwidth=1)
ax2_hist.set_xlabel('')
ax2_hist.set_ylabel('')
ax2_hist.set_yticks([])
ax2_hist.set_xticks([_lambda])

plt.suptitle('Boxplots example', fontsize=20)
plt.tight_layout()
plt.show()