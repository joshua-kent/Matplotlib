import matplotlib.pyplot as plt
import numpy as np

# style of graph, plt.style.available lists all possible
plt.style.use('seaborn-v0_8')

# constants
X_START_DATA = 2015
X_END_DATA = 2024.5
X_END_PROJECTION = 2030
PRECISION = 0.1

# produces data from X_START_DATA to X_END_DATA
x1 = np.arange(X_START_DATA, X_END_DATA + PRECISION, PRECISION)
y1 = np.sin(x1) + np.random.random(len(x1))*0.2
y1[-1] = np.sin(x1[-1])

# produces projected values (behaviour is manually described by y2)
x2 = np.arange(X_END_DATA, X_END_PROJECTION, PRECISION)
y2 = np.sin(x2)

# calculates absolute uncertainty using an arbitrary method
# to produce good illustrative uncertainties
y_err = np.exp(0.1 * (x2 - X_END_DATA)) - 1

fig = plt.figure()
ax = fig.add_subplot(111)

true_data, = ax.plot(x1, y1, 'k')
true_data.set_label("Historical data")
proj, = ax.plot(x2, y2, 'b')
proj.set_label("Projected data")
# plots the error band by filling between the two y values y2-y_err and y2+y_err,
# where y_err is the absolute uncertainty in the y values
ax.fill_between(x2, y2 - y_err, y2 + y_err, alpha=0.3)

# handles cosmetic changes to graph
ax.legend(handles=[true_data, proj])
ax.grid(visible=True)
ax.set_xlim(X_START_DATA, X_END_PROJECTION)
ax.set_xticks(np.arange(X_START_DATA, X_END_PROJECTION + 1, 1))
ax.set_title("A projection using an errorband")

plt.tight_layout()
plt.show()