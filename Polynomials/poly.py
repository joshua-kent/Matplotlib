import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np
import math
plt.rcParams['text.usetex'] = True # uses tex font

# creturns list of coefficients for power series for sine is x - x^3/3! + x^5/5! - x^7/7! etc.
def taylor_sine(n):
    k = 0
    p = []
    while k < 2*n:
        if k % 2 == 0:
            p.append(0)
        else:
            if k % 4 == 1:
                q = 0
            else:
                q = 1
            p.append((-1)**q * 1/(math.factorial(k)))
        k += 1
    return p
tay = lambda x: np.polynomial.Polynomial(taylor_sine(x))
x1 = np.arange(-10, 10, 0.1)
y1 = np.sin(x1)

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(left=0.25) # adds a 0.25 margin to make room for slider
plt.title(r'Taylor series expansions of $\sin x$', fontsize=25)
ax.plot(x1, y1, 'k', linewidth=2) # plots a sine curve

# power slider
ax_n = fig.add_axes([0.1, 0.15, 0.0225, 0.70])
n_slider = Slider(
    ax=ax_n,
    label='Power',
    valmin=0,
    valmax=10,
    valinit=0,
    orientation='vertical',
    valstep=1,
    color=(0.1,0.5,0.1),
    

)

# update sine Taylor polynomials upon updated slider
def update(val):
    # remove lines which are greater powers than 'val'
    for i in ax.lines:
        try: # ignores invalid gids (eg the sine curve with no gid)
            if int(i.get_gid()) > val:
                i.remove()
        except:
            continue

    # k is a list of the gids of all elements in ax.lines (each line)
    k = [ax.lines[m].get_gid() for m in range(len(ax.lines))]
    # if a gid is missing (labelled with power, so power 1 has gid=1, power 2 has gid=2, etc),
    # then add that line, with its corresponding gid.
    for i in range(1, val+1):
        if i not in k:
            ax.plot(x1, tay(i)(x1), "--", color=(0,0.5*(1-i/n_slider.valmax),0.5*(1-i/n_slider.valmax)), gid=i)
    fig.canvas.draw_idle()
n_slider.on_changed(update)

ax.set_ylim(top = 3.5, bottom = -3.5)
ax.set_xlabel(r'$x$', fontsize=20)
ax.set_ylabel(r'$\sin x$', fontsize=20)

ax.grid(True)
plt.show()