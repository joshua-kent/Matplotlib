import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

x_ = np.arange(-10, 10, 1)
y_ = np.arange(-10, 10, 1)
X = np.arange(10, -10, -1)
Y = np.arange(10, -10, -1)
U, V = np.meshgrid(X, Y)
color = np.sqrt(U**2 + V**2)
# try with more complicated example, such as a differential equation

q = ax.quiver(x_, y_, U,V, color)

plt.show()