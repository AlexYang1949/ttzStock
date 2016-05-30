import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize = (4,8))
plt.plot(x,y,label = '$sin(x)$')
plt.plot(x,z,"b--",label = '$cos(x)$')
plt.xlabel(("Time(s)"))
plt.ylabel((""))
plt.title("matplotlib")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

fig = plt.gcf()
ax = plt.gca()
print(fig)
print(ax)

#绘制常用图表
# 柱形图

