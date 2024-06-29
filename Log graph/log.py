import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

x1 = np.arange(5, 300, 1)
# plots a graph which should have a l.o.b.f. about y=4x+50
y1 = 4*x1 + np.random.randint(1, 100, len(x1))

# produces a linear regression line of the above data ()
reg = scipy.stats.linregress(x1, y1)
y2 = reg.slope * x1 + reg.intercept

plt.figure(num="Log and linear plots")
#plt.suptitle('Log and linear plots')

# linear graph
plt.subplot(221)
plt.plot(x1, y1, 'o', x1, y2, 'k--')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.ylabel('y')
plt.xlabel('x')
plt.yscale('linear') # (makes linear y-scale, the default)
plt.grid(True)
plt.title('Linear')
plt.annotate(f'$y={np.round(reg.slope,2)}x+{np.round(reg.intercept,2)}$', (50, 1000))

# log (base 10) graph
plt.subplot(222)
plt.plot(x1, y1, 'o', x1, y2, 'k--')
plt.ylim(bottom=10)
plt.xlim(left=0)
plt.ylabel('log y')
plt.xlabel('x')
plt.yscale('log') # (makes logarithmic y-scale, log base 10)
plt.grid(True)
plt.title('Log')

# log (base e) graph
plt.subplot(223)
plt.plot(x1, y1, 'o', x1, y2, 'k--')
plt.ylim(bottom=10)
plt.xlim(left=0)
plt.ylabel('ln y')
plt.xlabel('x')
plt.yscale('log', base=np.e) # (makes logarithmic y-scale, log base 10)
plt.grid(True)
plt.title('Ln')
exp_range_min, exp_range_max = 2,9
q = len(plt.yticks()[0])
plt.yticks([np.e**i for i in range(exp_range_min, exp_range_max)],
           ["".join((r"$e^", str(i), r"$")) for i in range(exp_range_min, exp_range_max)])
# this is to remark y-ticks in the format "e^2" rather than "2.71828...^2"


plt.tight_layout()
plt.show()