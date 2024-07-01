import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import colors
import numpy as np
import cmath

def julia(z, c, iters=500):
    f = lambda w, c1: w**2 + c1
    k = f(z,c)
    id = np.where(True, 0, k)
    for i in range(iters):
        k = f(k, c)
        q = np.abs(k)
        id = np.where(q > 10e6, i, id)
        k = np.where(q > 10e6, cmath.nan, k)
    id = np.where(id==0, np.max(id), id)
    return abs(id)

update_title = lambda : ax.set_title(f'Julia set, $z^2 + {np.round(c.real,2)} + {np.round(c.imag,2)}i$')

prec = 1200
iters = 100

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.3)

c = 0 + 0j
x_lims_j, y_lims_j = (-2, 2), (-2, 2)
x_j = np.linspace(x_lims_j[0], x_lims_j[1], round(prec/3))
y_j = np.linspace(y_lims_j[0], y_lims_j[1], round(prec/4))
xx_j, yy_j = np.meshgrid(x_j, y_j)
zz_j = xx_j + yy_j * 1j
zz_j_final = julia(zz_j, c, iters)

h_ax2 = ax.imshow(zz_j_final,
                   cmap='seismic',
                   extent=[x_lims_j[0], x_lims_j[1], y_lims_j[0], y_lims_j[1]],
                   norm='log')
ax.axis('off')


ax_re = fig.add_axes([0.1, 0.20, 0.8, 0.10])
re_slider = Slider(
    ax=ax_re,
    label='Real',
    valmin=-2,
    valmax=2,
    valinit=0,
    orientation='horizontal',
    valstep=0.05,
    color=(0.1,0.5,0.1)
)
ax_im = fig.add_axes([0.1, 0.1, 0.8, 0.10])
im_slider = Slider(
    ax=ax_im,
    label='Imaginary',
    valmin=-2,
    valmax=2,
    valinit=0,
    orientation='horizontal',
    valstep=0.05,
    color=(0.1,0.5,0.1)
)
ax_res = fig.add_axes([0.1, 0.0, 0.8, 0.10])
res_slider = Slider(
    ax=ax_res,
    label='Resolution',
    valmin=500,
    valmax=5000,
    valinit=1000,
    orientation='horizontal',
    valstep=500,
    color=(0.1,0.5,0.1)
)

def update_re(val):
    global c, iters
    c = val + c.imag * 1j
    zz_j_final = julia(zz_j, c, iters)
    h_ax2.set_data(zz_j_final)
    update_title()
def update_im(val):
    global c, iters
    c = c.real + val * 1j
    zz_j_final = julia(zz_j, c, iters)
    h_ax2.set_data(zz_j_final)
    update_title()
def update_res(val):
    global prec, x_j, y_j, xx_j, yy_j, zz_j, zz_j_final, c, iters
    prec = val
    x_j = np.linspace(x_lims_j[0], x_lims_j[1], round(prec/3))
    y_j = np.linspace(y_lims_j[0], y_lims_j[1], round(prec/4))
    xx_j, yy_j = np.meshgrid(x_j, y_j)
    zz_j = xx_j + yy_j * 1j
    zz_j_final = julia(zz_j, c, iters)
    h_ax2.set_data(zz_j_final)

re_slider.on_changed(update_re)
im_slider.on_changed(update_im)
res_slider.on_changed(update_res)

update_title()
plt.show()