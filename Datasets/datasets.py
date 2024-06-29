import matplotlib.pyplot as plt
import numpy as np

# number of datapoints in dataset 'data'
amt = 2000

# transforms standard normal (randn) to a random variable with std dev 'dev' and mean 'mean',
# there are 'amt' of these in the tuple
dev = 2
mean = 100
Y = dev * np.random.randn(amt) + mean

data = {
    # produces x values from 0 to amt-1
    'x': np.arange(amt),
    # produces corresponding y values, normally distributed
    'y': Y,
    's': np.random.randint(1,20,amt),
    # 'c' is colours, listed as RGB(A) values in [0,1] intervals
    'c': [(1 - 0.9*np.random.rand(), 0.1, 0.1) for i in range(amt)]
}

# x values, y values, size (of dots on scatter graph), colours, dataset
plt.scatter(x='x', y='y', s='s', c='c', data = data)
# set axes to [0, amt] on x-axis and [min(Y) - 0.2*abs(min(Y)), 1.2*max(Y)] on y-axis
plt.axis((0, amt, min(Y)-0.2*abs(min(Y)), 1.2*max(Y)))
# display grid lines
plt.grid(True)
# title
plt.title('Datasets example')
# show graph
plt.show()