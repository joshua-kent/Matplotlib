import matplotlib.pyplot as plt
import numpy as np
import math
plt.rcParams['text.usetex'] = True

# power series for sine is x - x^3/3! + x^5/5! - x^7/7! etc.
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
plt.title(r'Taylor series expansions of $\sin x$', fontsize=25)
plt.plot(x1, y1, 'k')
n=6
for i in range(1,n):
    plt.plot(x1, tay(i)(x1), '--')
plt.ylim(top = 3.5, bottom = -3.5)
plt.xlabel(r'$x$', fontsize=20)
plt.ylabel(r'$\sin x$', fontsize=20)

plt.grid(True)
plt.show()