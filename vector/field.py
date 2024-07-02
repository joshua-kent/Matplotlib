import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

np.seterr(divide='ignore', invalid='ignore') # ignores division by zero error message

fig = plt.figure()
ax = fig.add_subplot()

x_axes_limits = (-15, 15)
y_axes_limits = (-15, 15)
step = 0.5

# produces arrays for x,y-coordinate plane
X, Y = np.meshgrid(np.arange(x_axes_limits[0], x_axes_limits[1], step),
                   np.arange(y_axes_limits[0], y_axes_limits[1], step))

# [q, (x, y)]
charges = ([1.0, (-5.0, 0.0)],
           [1.0, (5.0, 0.0)],
           [-1.0, (0.0, 5.0)],
           [-1.0, (0.0, -5.0)])

# force represents the array of resultant forces at each point
# as complex numbers (real = x, imag = y)
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

# to set colour of +ve charges red, -ve charged blue
def charge_colour[real](q: real) -> str:
    if np.sign(q) == 1: # positive charge
        return 'r'
    else:
        return 'b'
# used to add +ve, -ve into legend (without directly assigning a 'patch' ie the circles)
positive_patch = mpatches.Patch(color='r', label='Positive')
negative_patch = mpatches.Patch(color='b', label='Negative')

# plot stream field
q = ax.streamplot(X,Y,U,V, density=1.5, broken_streamlines=True, color=color, cmap='inferno')
# plot circles for charges
for q, pos in charges:
    ax.add_artist(mpatches.Circle(pos, 0.5, color=charge_colour(q)))

# charges legend
ax.legend(handles=[positive_patch, negative_patch], title="Charges")

ax.set_aspect('equal') # sets aspect ratio as a square (so circles do not appear as ellipses)
ax.set_xlim(left=x_axes_limits[0], right=x_axes_limits[1])
ax.set_ylim(bottom=y_axes_limits[0], top=y_axes_limits[1])
ax.set_title("Electric field about point charges")
plt.show()