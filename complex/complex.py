import matplotlib.pyplot as plt
import numpy as np
import cmath

def mandelbrot(z, iters=500):
    f = lambda w, c: w**2 + c

    k = f(0,z)
    id = np.where(True, 0, k)
    for i in range(iters):
        k = f(k, z)
        q = np.abs(k)
        id = np.where(q > 10000, i, id)
        k = np.where(q > 10000, cmath.nan, k)
    id = np.where(id==0, np.max(id), id)
    return np.float64(abs(id))

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


prec = 2000

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# mandelbrot
x_lims_m, y_lims_m = (-2.5, 1.5), (-2, 2)
x_m = np.linspace(x_lims_m[0], x_lims_m[1], round(prec/3))
y_m = np.linspace(y_lims_m[0], y_lims_m[1], round(prec/4))
xx_m, yy_m = np.meshgrid(x_m, y_m)
zz_m = xx_m + yy_m * 1j
zz_m_final = mandelbrot(zz_m, 200)

h_ax1 = ax1.imshow(zz_m_final,
                   cmap='copper',
                   extent=[x_lims_m[0], x_lims_m[1], y_lims_m[0], y_lims_m[1]],
                   norm='log')
ax1.axis('off')
ax1.set_title('Mandelbrot set')

# julia
c = -0.8 + 0.156j
x_lims_j, y_lims_j = (-2, 2), (-2, 2)
x_j = np.linspace(x_lims_j[0], x_lims_j[1], round(prec/3))
y_j = np.linspace(y_lims_j[0], y_lims_j[1], round(prec/4))
xx_j, yy_j = np.meshgrid(x_j, y_j)
zz_j = xx_j + yy_j * 1j
zz_j_final = julia(zz_j, c, 200)

h_ax2 = ax2.imshow(zz_j_final,
                   cmap='copper',
                   extent=[x_lims_j[0], x_lims_j[1], y_lims_j[0], y_lims_j[1]],
                   norm='log')
ax2.axis('off')
ax2.set_title(f'Julia set, $z^2 + {c.real} + {c.imag}i$')


plt.tight_layout()
plt.show()
