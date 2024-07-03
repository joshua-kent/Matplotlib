import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

# defines range of values used for parameter t
t = np.arange(0, 12 * np.pi, 0.01)

# defines x and y in terms of t (for each value of t described above), as an array
x = np.sin(t) * ( np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
y = np.cos(t) * ( np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)

ax.plot(x, y, 'k')

ax.set_aspect('equal')
ax.set_title("The butterfly curve")

plt.show()