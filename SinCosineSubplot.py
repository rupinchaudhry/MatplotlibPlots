# Using Subplot
import numpy as np
import matplotlib.pyplot as plt

x =  np.arange(0.0, 1.0, 0.01)
y1 = np.sin(8*np.pi*x)
y2 = np.cos(8*np.pi*x)
fig = plt.figure(figsize=(15,7))
ax1 = plt.subplot(121); ax1.plot(x, y1, 'red'); ax1.set_title("Sine wave")
ax2 = plt.subplot(122); ax2.plot(x, y2, 'blue'); ax2.set_title("Cosine wave")
plt.suptitle("Trigonometric functions")
plt.show()
