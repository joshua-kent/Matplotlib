import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x = np.random.uniform(-4, 4, 256)
y = np.random.uniform(-4, 4, 256)
z = np.sin(x) + np.sin(y)
# splits into 10 contour regions
levels = np.linspace(z.min(), z.max(), 10)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(x, y, 'o', markersize = 2, color = "lightgrey")
# creates a contour with appropriate levels
contour_nf = ax1.tricontour(x, y, z, levels=levels)
ax1.set(xlim = (-3, 3),
        ylim = (-3, 3),
        title = "Contour map (unfilled)")

ax2.plot(x, y, 'o', markersize = 2, color = "lightgrey")
contour_f = ax2.tricontourf(x, y, z, levels=levels)
ax2.set(xlim = (-3, 3),
        ylim = (-3, 3),
        title = "Contour map (filled)")

# colour bar for (either) contour
cbar = fig.colorbar(contour_f)

plt.show()