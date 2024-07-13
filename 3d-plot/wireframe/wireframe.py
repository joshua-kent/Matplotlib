import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

plt.style.use('_mpl-gallery')

x, y, z = axes3d.get_test_data(0.03)

fig = plt.figure("Wireframe")
ax = fig.add_subplot(111, projection='3d')

# draws wireframe using the test data
axes3d.Axes3D.plot_wireframe(ax, x, y, z, rstride=10, cstride=10, color="#2020b0")

plt.show()