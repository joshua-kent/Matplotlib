import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# produces a polar graph
ax = fig.add_subplot(111, projection='polar')

# defines theta and r
theta = np.arange(0, 2*np.pi,0.01)
r = np.sin(5*theta) + 2

plt.title(r"$r = \sin 5\theta + 2$")

# plots theta and r
ax.plot(theta, r, linewidth=2, color='red')

# sets y-ticks
ax.set_yticks(np.arange(0,4,1))
ax.set_rlabel_position(0)
ax.set_ylim(top=4)

plt.show()