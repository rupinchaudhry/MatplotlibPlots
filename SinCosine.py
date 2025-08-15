# Using Subplots
import numpy as np
import matplotlib.pyplot as plt

x =  np.arange(0.0, 1.0, 0.01)
y1 = np.sin(8*np.pi*x)
y2 = np.cos(8*np.pi*x)
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(15,7))
ax[0].plot(x, y1); ax[0].set_title("Sine wave")
ax[1].plot(x, y2); ax[1].set_title("Cosine wave")
plt.suptitle("Trigonometric functions")
plt.show()
