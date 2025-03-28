import os
import numpy as np

# h0_list = np.logspace(np.log10(0.2e-3), np.log10(1e-3), 100)
h0_list = [0.3e-3]
st_list = [42e-3]
viscosity_list = [1e-2]
L_list = np.logspace(np.log10(0.01), np.log10(.1), 30)  # L from 0.2 to 1.0 in 5 steps
theta_s_list = [17.4]
kappa_list = [2.2e-4]


folder = r"G:\My Drive\Research projects\WPM\Data\Simulation\parameters\length"

for kappa, theta_s in zip(kappa_list, theta_s_list):
    for mu in viscosity_list:
        for sigma in st_list:
            for h0 in h0_list:
                for L in L_list:
                    # print the file name
                    N = max(500, int(1000 * L / 0.2))
                    filename = f'mu_{mu:.2e}_sigma_{sigma:.2e}_h0_{h0:.2e}_L_{L:.2e}.csv'
                    print(filename)
                    # Run the simulation
                    fileDir = os.path.join(folder, filename)
                    os.system(f'python dimple_simulation.py \"{fileDir}\" --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e} -X {L:.2e} -T 200 -s 0.1 -N {N:d}')