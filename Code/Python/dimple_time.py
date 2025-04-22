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

    # read the surface profile data
    df = pd.read_hdf(i.Dir)
    # initialize lists to store minima and maxima
    t_list = []
    minima_list = []
    maxima_list = []
    minima_index_list = []
    maxima_index_list = []
    curvature_minima = []
    curvature_maxima = []
    mean_surface_height_list = []
    Pg = []
    Pc = []
    ld = []
    Vm_list = []

    # infer the max time from the column names, for coloring the curves
    tmax = float(df.columns[-1])
    cmap = plt.get_cmap("viridis")
    
    j = 0
    
    for kw in df:
        # infer time
        t = float(kw)

        # read surface profile data for smoothing purpose
        x, y = df.index, df[kw].values

        # compute the second derivative
        dy = np.gradient(y, x)
        d2y = np.gradient(dy, x)

        # Find local minima in the filtered data, exclude the first last points
        minima_indices = argrelextrema(y, np.less)
        maxima_indices = argrelextrema(y, np.greater)

        # record the data
        t_list.append(t)
        # it could be the case that there is no minima or maxima. In such cases, we record np.nan in the place.
        if len(minima_indices[0]) > 0 and len(maxima_indices[0]) > 0:
            minima_index, maxima_index = int(minima_indices[0][0]), int(maxima_indices[0][0])
            minima_index_list.append(minima_index)
            maxima_index_list.append(maxima_index) 
            minima_list.append(y[minima_index])
            maxima_list.append(y[maxima_index])
            curvature_minima.append(d2y[minima_index])
            curvature_maxima.append(d2y[maxima_index])
            Pg.append(rho * g * (y[maxima_index]-y[minima_index]) * 1e-3)
            Pc.append(sigma * d2y[minima_index] * 1e3)
            ld.append(x[minima_index]*1e3)
            h = y[:minima_index]
            Vm_list.append(integrate.trapezoid(h-y[minima_index], x=x[:minima_index]))
        else:
            minima_list.append(np.nan)
            minima_index_list.append(np.nan)
            curvature_minima.append(np.nan)
            maxima_list.append(np.nan)
            maxima_index_list.append(np.nan)
            curvature_maxima.append(np.nan)
            Pg.append(np.nan)
            Pc.append(np.nan)
            ld.append(np.nan)
            Vm_list.append(np.nan)

        mean_surface_height_list.append(y.mean())

    # save dimple data to file
    dimple = pd.DataFrame(data={"t": t_list, 
                                "minima": minima_list, 
                                "maxima": maxima_list, 
                                "minima_index": minima_index_list, 
                                "maxima_index": maxima_index_list,
                                "curvature_minima": curvature_minima,
                                "curvature_maxima": curvature_maxima,
                                "mean_surface_height": mean_surface_height_list,
                                "Pg": Pg,
                                "Pc": Pc,
                                "ld": ld,
                                "Vm": Vm_list,})
    dimple.to_csv(os.path.join(dimple_folder, i.Name+".csv"), index=False)

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
            pg = dimple.Pg
            pc = dimple.Pc
            ld = dimple.ld
            Vm = dimple.Vm
            hmin = dimple.minima
            hmax = dimple.maxima
            # h = df.iloc[:int(dimple.minima_index), np.argmin(np.abs(df.columns.astype(float)-i.t))]
            # Vm = integrate.trapezoid(h-i.h0*1e3, x=h.index)
        else:
            t = np.nan
            pg = np.nan
            pc = np.nan
            ld = np.nan
            hmin = np.nan
            hmax = np.nan
            Vm = np.nan
    else:
        t = np.nan
        pg = np.nan
        pc = np.nan
        ld = np.nan
        hmin = np.nan
        hmax = np.nan
        Vm = np.nan

    dimple_time_list.append(tmp | {"t": t} | {"pg": pg} | {"pc": pc} | {"ld": ld} |  {"hmin": hmin} | {"hmax": hmax} | {"Vm": Vm})
    dimple_time = pd.DataFrame(dimple_time_list)
    dimple_time.to_csv(os.path.join(dimple_folder, "dimple_time.csv"), index=False)

    print(time.asctime() + " -> " + i.Name)

    if args.plot:
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
        for minima_index, minima in zip(minima_index_list[25::down_sample], minima_list[25::down_sample]):
            if np.isnan(minima_index):
                continue
            ax[0][0].scatter(df.index[minima_index], minima, color="blue", s=5, zorder=10)
        for maxima_index, maxima in zip(maxima_index_list[25::down_sample], maxima_list[25::down_sample]):
            if np.isnan(maxima_index):
                continue
            ax[0][0].scatter(df.index[maxima_index], maxima, color="red", s=5, zorder=10)
        
        # plot minima and maxima
        ax[0][1].plot(t_list, minima_list, color="blue", lw=2)
        ax[0][1].plot(t_list, maxima_list, color="red", lw=2)
        ax[0][1].set_xlim([0, tmax])
        ax[0][1].set_ylim([0, df.max().max()])
        ax[0][1].set_xlabel("Time, $t$ (s)")
        ax[0][1].set_ylabel("Surface height, $h$ (mm)")

        # plot mean surface height vs. time
        ax[1][0].plot(t_list, mean_surface_height_list, color="black", lw=2)
        ax[1][0].set_xlim([0, tmax])
        ax[1][0].set_ylim([0, df.max().max()])
        ax[1][0].set_xlabel("Time, $t$ (s)")
        ax[1][0].set_ylabel("Mean surface height, $h_{mean}$ (mm)")

        # plot curvatures at minima and maxima
        ax[1][1].plot(t_list, curvature_minima, color="blue", lw=2)
        ax[1][1].plot(t_list, curvature_maxima, color="red", lw=1)
        ax[1][1].set_xlim([0, tmax])
        ax[1][1].set_ylim([-0.1, 0.1])
        ax[1][1].set_xlabel("Time, $t$ (s)")
        ax[1][1].set_ylabel("Curvature, $\kappa$ (mm$^{-1}$)")

        plt.tight_layout()
        fig.savefig(os.path.join(dimple_folder, i.Name+".jpg"), bbox_inches="tight")
        plt.close()

