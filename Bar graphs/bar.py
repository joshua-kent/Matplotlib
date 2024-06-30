import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (1 + x**2)**(-0.5)

x1 = np.arange(-10, 10, 0.1)
x1f = np.arange(-10, 10, 2)
x2 = np.arange(-10, 10, 1)

plt.figure()
# 1 row, 2 columns, first subplot (of 2)
plt.subplot(1, 2, 1)
plt.plot(x1, f(x1), 'k')
plt.ylim(bottom=0)
plt.vlines(x1f, 0, f(x1f), colors=[(i/len(x1f),0,0) for i in range(len(x1f))])
plt.axes((-10,10,0.0, 1.5*max(x1)))

# 1 row, 2 columns, second subplot (simplified notation)
plt.subplot(122)
plt.plot(x1, f(x1), 'k--')
plt.bar(x2, f(x2))
plt.axes((-10,10,0.0, 1.5*max(x1)))

plt.suptitle("$y= \\frac{1}{\\sqrt{1+x^2}}$ graphs", fontsize=20)

plt.show()