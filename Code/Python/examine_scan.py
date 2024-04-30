import matplotlib.pyplot as plt
import pandas as pd

surface = pd.read_csv(r"E:\WPM\04292024\beet_scan_2.csv", usecols=[1], skiprows=12, names=["height"])
plt.plot(surface)
plt.show()