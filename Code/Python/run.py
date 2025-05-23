import os
import numpy as np
import time

sigma_list = [42e-3] # sigma from 0.01 to 0.1 in 5 steps
mu_list = [10e-3]
theta_s_list = [17.4]
kappa_list = [2.2e-4]
h0_list = np.linspace(0.2e-3, 0.4e-3, 20)
L_list = np.linspace(100, 200, 20)



folder = r"C:\Users\zl948\Documents\WPM_simulation\LH_PD"

for kappa, theta_s, mu, sigma in zip(kappa_list, theta_s_list, mu_list, sigma_list):
    for h0 in h0_list:
        for L in L_list:
            # print the file name
            N = 500
            filename = f'mu_{mu:.2e}_sigma_{sigma:.2e}_h0_{h0:.2e}_L_{L:.2e}.h5'
            print(time.asctime() + " -> " + filename)
            # Run the simulation
            fileDir = os.path.join(folder, filename)
            if os.path.exists(fileDir):
                print(f"File {filename} already exists, skipping.")
                continue
            os.system(f'python dimple_simulation.py \"{fileDir}\" --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e} -X {L:.2e} -T 1000 -s 0.1 -N {N:d} --tscale linear -s 1')