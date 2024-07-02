import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

x_lims = (-10, 10)
y_lims = (-10, 10)
step = 0.5

x, y = np.meshgrid(np.arange(x_lims[0], x_lims[1], step),
                   np.arange(y_lims[0], y_lims[1], step))

# y = e^(-sin^2 x) + C
u = 1
v = -2 * np.sin(2 * x)  * np.exp(- ( np.sin(x) ) ** 2)
uv_len = np.sqrt(u**2 + v**2)

u, v = u/uv_len, v/uv_len # normalise vectors (keeps size of each vector same in quiver)

# plots the vectors, with a cool-warm colour scheme
ax.quiver(x, y, u, v, np.log(uv_len), cmap='coolwarm', pivot ='mid')
# single stream plot for illustration
ax.streamplot(x, y, u, v, broken_streamlines=False, start_points=[(0,0)], color='k', linewidth=2)

ax.set_title("$\\frac{\\mathrm{d}y}{\\mathrm{dx}} = -2 \\sin(2x) e^{-\\sin^2 x}$")
ax.set_xlim(left=x_lims[0], right=x_lims[1])
ax.set_ylim(bottom=y_lims[0], top=y_lims[1])

plt.show()
