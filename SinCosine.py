import numpy as np
import matplotlib.pyplot as plt

x =  np.arange(0, 50, 1)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(15,7))
ax[0].plot(x, y1); ax[0].set_title("Sine wave")
ax[1].plot(x, y2); ax[1].set_title("Cosine wave")
plt.suptitle("Trigonometric functions")
plt.show()
