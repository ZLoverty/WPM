import matplotlib.pyplot as plt
import pandas as pd
import sys

data_path = sys.argv[1]
surface = pd.read_csv(data_path, usecols=[1], skiprows=12, names=["height"])
plt.plot(surface)
plt.show()