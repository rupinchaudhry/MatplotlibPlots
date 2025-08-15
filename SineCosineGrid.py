# Using Subplot2Grid
import numpy as np
import matplotlib.pyplot as plt

x =  np.arange(0.0, 1.0, 0.01)
y1 = np.sin(8*np.pi*x)
y2 = np.cos(8*np.pi*x)
y3 = y1/y2
ax = []
fig = plt.figure(figsize=(15,7))
ax.append(plt.subplot2grid((3,3), (0,0), colspan=3))
ax.append(plt.subplot2grid((3,3), (1,0), rowspan=2, colspan=2))
ax.append(plt.subplot2grid((3,3), (1,2), rowspan=2, colspan=1))
ax[0].plot(x, y1, 'red'); ax[0].set_title("Sine wave")
ax[1].plot(x, y2, 'blue'); ax[1].set_title("Cosine wave")
ax[2].plot(x, y3, 'green'); ax[2].set_title("Tan wave")
plt.suptitle("Trigonometric functions")
plt.show()
