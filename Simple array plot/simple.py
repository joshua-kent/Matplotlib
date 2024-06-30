import matplotlib.pyplot as plt
import numpy as np

start = 0
step = 0.2
final = 4

# use numpy to produce an array of values between start and final, with step 'step'
t = np.arange(start,final,step)

# plots a y=x graph, a y=sqrt(x) graph, and a y=e^x ingraph
plt.plot(t, t, 'r--', t, t**0.5, 'bs', t, np.e**t, 'g^')

# -- dash
# s square
# o circle
# ^ triangle
plt.show()