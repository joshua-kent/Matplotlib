import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

datapoints=1000
data = {
    'x': np.arange(0, datapoints, 1),
    'y': np.append(np.random.normal(10,5,int(datapoints/2)),np.random.poisson(12,int(datapoints/2))),
    'class': np.append(np.full(int(datapoints/2), 'A'), np.full(int(datapoints/2), 'B'))
}

print(f"x:{data['x']}\ny:{data['y']}\nclass:{data['class']}")

ax1.scatter(x='x',y='y', data=data)
sns.boxplot(data=data, x='y', y='class', ax=ax2,showfliers=False, fill=False,color="r")
#ax2.set_xlim(left=-20,right=20)
#ax.set_xticks([i for i in np.arange(0,101,1) if i%20==0])


plt.show()