import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

np.seterr(invalid='ignore') # ignores division by zero error message

fig = plt.figure()
ax = fig.add_subplot()

x_axes_limits = (-15, 15)
y_axes_limits = (-15, 15)
step = 0.5

X, Y = np.meshgrid(np.arange(x_axes_limits[0], x_axes_limits[1], step),
                   np.arange(y_axes_limits[0], y_axes_limits[1], step))

charges = ([1, (-5,0)], [1, (5,0)], [-1, (0, 5)], [-1, (0, -5)])

force = 0
for q, pos in charges:
    charge_x = (X - pos[0])
    charge_y = (Y - pos[1])
    charge_complex = charge_x + charge_y * 1j
    distance = abs(charge_complex)
    # v     applies inverse square law, first divide by distance to normalise to direction vector
    #       then divide by squared distance
    force_contribution = q * charge_complex / (distance ** 3)
    force += force_contribution

U = force.real
V = force.imag

color = np.log(np.sqrt(U**2 + V**2))

def charge_colour(q):
    if np.sign(q) == 1: # positive charge
        return 'r'
    else:
        return 'b'

q = ax.streamplot(X,Y,U,V, density=1.5, broken_streamlines=True, color=color, cmap='inferno')
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.5, color=charge_colour(q)))

ax.set_aspect('equal')
ax.set_xlim(left=x_axes_limits[0], right=x_axes_limits[1])
ax.set_ylim(bottom=y_axes_limits[0], top=y_axes_limits[1])
plt.show()