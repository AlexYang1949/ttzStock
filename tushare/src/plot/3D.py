from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')
th = np.linspace(-4*np.pi, 4*np.pi,10)
z = np.linspace(-2, 0, 10)
r = z**2 +1
x = r * np.sin(th)
y = r*np.cos(th)

ax.plot(x,y,z,label='hello')
ax.legend()
plt.show()