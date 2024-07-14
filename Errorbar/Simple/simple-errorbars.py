import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3, 0.2)
y = np.exp(x)

fig = plt.figure()
ax = fig.add_subplot(111)

y_errs = 0.1 + np.sqrt(y)
x_errs = 0.05

# produces errorbars
ax.errorbar(x = x,
            y = y,
            yerr = y_errs,
            xerr = x_errs,
            marker='x',
            capsize=5,
            ecolor='k')

ax.set_title("Simple errorbars")
ax.grid(visible = True)

plt.show()