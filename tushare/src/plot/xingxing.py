from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


plt.figure()

x = np.random.random(100)
y = np.random.random(100)

plt.scatter(x, y,s=(x + 10)*100,c=y,marker=(5,1),lw=2,facecolor = 'none')

plt.xlim()
plt.ylim()
plt.show()

