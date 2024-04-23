import numpy as np
import matplotlib.pyplot as plt

plt.ion()
for i in range(100):
    x = np.linspace(i, i+3)
    y = np.sin(x)
    plt.plot(x, y)
    plt.draw()
    plt.pause(.1)
