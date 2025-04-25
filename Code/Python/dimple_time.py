"""
dimple_time.py
==============

Compute the dimple time of all the surface evolution data in a folder.

Syntax
------

python dimple_time.py folder

Edit
----
Apr 16, 2025: Initial commit.
Apr 23, 2025: (i) Add gravity length scale to the dimple time computation. (ii) Reorganize the code with functions: each function will compute one thing, and if it is not available, it will return NaN.
"""

import argparse
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from myimagelib import readdata
from scipy import integrate
import time

def find_first_h0(h, h0):
    """
    Find the first h0 index.
    """
    h = np.array(h)

    inds = h >= h0
    # find the first true in inds
    if np.any(inds):
        first_h0 = np.where(inds)[0][0]
    else:
        first_h0 = np.nan
    return first_h0

def compute_minima_maxima(x, y):
    """
    Compute the minima and maxima of the surface profile.
    """
    # Find local minima in the filtered data, exclude the first last points
    minima_indices = argrelextrema(y, np.less)
    maxima_indices = argrelextrema(y, np.greater)
    # compute the second derivative
    dy = np.gradient(y, x)
    d2y = np.gradient(dy, x)
    if len(minima_indices[0]) > 0 and len(maxima_indices[0]) > 0:
        minima_index, maxima_index = int(minima_indices[0][0]), int(maxima_indices[0][0])
        minima, maxima = y[minima_index], y[maxima_index]
        curvature_minima, curvature_maxima = d2y[minima_index], d2y[maxima_index]
        pressure_gravity = rho * g * (maxima - minima) * 1e-3
        pressure_curvature = sigma * d2y[minima_index] * 1e3
        ld = x[minima_index]
        hbulk = y[minima_index:]
        h0_ind = find_first_h0(hbulk, h0*1e3)
        if np.isnan(h0_ind):
            lm = np.nan
        else:
            lm = (x[h0_ind+minima_index] - x[minima_index])
        h = y[:minima_index]
        Vm = integrate.trapezoid(h-y[minima_index], x=x[:minima_index])
    else:
        minima_index, maxima_index = np.nan, np.nan
        minima, maxima = np.nan, np.nan
        curvature_minima, curvature_maxima = np.nan, np.nan
        pressure_gravity, pressure_curvature = np.nan, np.nan
        ld, lm = np.nan, np.nan
        Vm = np.nan

    return {"minima": minima, "maxima": maxima, "minima_index": minima_index, "maxima_index": maxima_index, "pg": pressure_gravity, "pc": pressure_curvature, "ld": ld, "lm": lm, "Vm": Vm, "curvature_minima": curvature_minima, "curvature_maxima": curvature_maxima}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dimple time computation')
    parser.add_argument('folder', type=str, help='Folder to save the solution')
    parser.add_argument('--plot', type=bool, default=False, help='Plot the results')
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    rho = 1e3
    g = 9.81

    dimple_folder = os.path.join(folder, "dimple_detection")
    os.makedirs(dimple_folder, exist_ok=True)
    l = readdata(folder, "h5")

    dimple_time_list = []
    # loop through each surface profile data
    for num, i in l.iterrows():
        if os.path.exists(os.path.join(dimple_folder, i.Name+".csv")):
            print(f"{i.Name} already exists, skipping ...")
            continue
        # read file name for parameters
        sigma = float(i.Name.split("_")[3])
        h0 = float(i.Name.split("_")[5])

        # initialize data list
        data = []

        # read the surface profile data
        df = pd.read_hdf(i.Dir)

        j = 0
        
        for kw in df:
            # infer time
            t = float(kw)

            # read surface profile data for smoothing purpose
            x, y = df.index, df[kw].values
            
            # compute minima and maxima
            tmp_data = compute_minima_maxima(x, y)

            data.append({"t": t} | tmp_data | {"mean_surface_height": y.mean()})

        # save dimple data to file
        dimple = pd.DataFrame(data=data)
        dimple.to_csv(os.path.join(dimple_folder, i.Name+".csv"), index=False)

      

        print(time.asctime() + " -> " + i.Name)

        if args.plot:
            # infer the max time from the column names, for coloring the curves
            tmax = float(df.columns[-1])
            cmap = plt.get_cmap("viridis")

            # generate a report for each dimple detection
            fig, ax = plt.subplots(2, 2, figsize=(7,6), dpi=300)

            # plot the surface profile
            # down sample the data for plotting
            down_sample = 50
            for kw in df.columns[25::down_sample]:
                # read surface profile data for smoothing purpose
                x, y = df.index, df[kw].values
                ax[0][0].plot(x, y, color=cmap(float(kw)/tmax), lw=2)

            ax[0][0].set_xlim([0, df.index[-1]])
            ax[0][0].set_ylim([0, df.max().max()])
            ax[0][0].set_xlabel("Distance, $x$ (mm)")
            ax[0][0].set_ylabel("Surface height, $h$ (mm)")

            # label the minima and maxima points on the surface profile
            for minima_index, minima in zip(dimple.minima_index[25::down_sample], dimple.minima[25::down_sample]):
                if np.isnan(minima_index):
                    continue
                ax[0][0].scatter(df.index[minima_index], minima, color="blue", s=5, zorder=10)
            for maxima_index, maxima in zip(dimple.maxima_index[25::down_sample], dimple.maxima[25::down_sample]):
                if np.isnan(maxima_index):
                    continue
                ax[0][0].scatter(df.index[maxima_index], maxima, color="red", s=5, zorder=10)
            
            # plot minima and maxima
            ax[0][1].plot(dimple.t, dimple.minima, color="blue", lw=2)
            ax[0][1].plot(dimple.t, dimple.maxima, color="red", lw=2)
            ax[0][1].set_xlim([0, tmax])
            ax[0][1].set_ylim([0, df.max().max()])
            ax[0][1].set_xlabel("Time, $t$ (s)")
            ax[0][1].set_ylabel("Surface height, $h$ (mm)")

            # plot mean surface height vs. time
            ax[1][0].plot(dimple.t, dimple.mean_surface_height, color="black", lw=2)
            ax[1][0].set_xlim([0, tmax])
            ax[1][0].set_ylim([0, df.max().max()])
            ax[1][0].set_xlabel("Time, $t$ (s)")
            ax[1][0].set_ylabel("Mean surface height, $h_{mean}$ (mm)")

            # plot curvatures at minima and maxima
            ax[1][1].plot(dimple.t, dimple.curvature_minima, color="blue", lw=2)
            ax[1][1].plot(dimple.t, dimple.curvature_maxima, color="red", lw=1)
            ax[1][1].set_xlim([0, tmax])
            ax[1][1].set_ylim([-0.1, 0.1])
            ax[1][1].set_xlabel("Time, $t$ (s)")
            ax[1][1].set_ylabel("Curvature, $\kappa$ (mm$^{-1}$)")

            plt.tight_layout()
            fig.savefig(os.path.join(dimple_folder, i.Name+".jpg"), bbox_inches="tight")
            plt.close()

    # generate dimple_time.csv

    # read dimple data
    l = readdata(dimple_folder, "csv")

    for num, i in l.iterrows():

        dimple = pd.read_csv(i.Dir)

        # find dimple time
        ts = dimple.loc[dimple["minima"] / dimple["maxima"] <= 0.5, "t"]
        
        # analyze file name
        fields = i.Name.split("_")
        tmp = {}
        for j in range(0, len(fields), 2):
            tmp[fields[j]] = fields[j+1]

        if len(ts) != 0:
            tmin = dimple.loc[np.argmin(dimple["minima"] / dimple["maxima"]), "t"]
            t = ts.iloc[-1]
            if t > tmin:
                dimple = dimple.loc[np.argmin(np.abs(dimple["t"] - t))]
                pg = dimple.pg
                pc = dimple.pc
                ld = dimple.ld
                Vm = dimple.Vm
                hmin = dimple.minima
                hmax = dimple.maxima
                lm = dimple.lm
            else:
                t = np.nan
                pg = np.nan
                pc = np.nan
                ld = np.nan
                hmin = np.nan
                hmax = np.nan
                Vm = np.nan
                lm = np.nan
        else:
            t = np.nan
            pg = np.nan
            pc = np.nan
            ld = np.nan
            hmin = np.nan
            hmax = np.nan
            Vm = np.nan
            lm = np.nan

        dimple_time_list.append(tmp | {"t": t} | {"pg": pg} | {"pc": pc} | {"ld": ld} | {"lm": lm} | {"hmin": hmin} | {"hmax": hmax} | {"Vm": Vm})

    dimple_time = pd.DataFrame(dimple_time_list)
    dimple_time.to_csv(os.path.join(dimple_folder, "dimple_time.csv"), index=False)