import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

plt.style.use('_mpl-gallery')

x, y = np.meshgrid(np.arange(-10, 10, 0.1),
                   np.arange(-10, 10, 0.1))
z = np.exp(np.sin(x) + np.sin(y))

fig = plt.figure("Surface")
ax = fig.add_subplot(111, projection='3d')
surface = axes3d.Axes3D.plot_surface(ax, x, y, z, vmin=z.min(), cmap="inferno")

# adds colour bar
cbar = fig.colorbar(surface, ax=ax, location="left", shrink=0.8)

plt.show()