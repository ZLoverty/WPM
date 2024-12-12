import os
import numpy as np

h0_list = np.logspace(np.log10(0.2e-3), np.log10(1e-3), 100)
# viscosity_list = [1e-3, 10e-3, 15e-3, 1.7e-3, 3.6e-3, 10.5e-3, 58e-3]
# st_list = [72e-3, 42e-3, 23e-3, 68e-3, 66e-3, 64e-3, 62e-3]
# h0_list = [4e-4]
# viscosity_list = [x*1e-2 for x in range(1, 6)]
# st_list = [4e-2]
# L_list = [0.5e-2*x for x in range(5, 6)]
# mu = 1e-2
# sigma = 0.042
# kappa = 0.05    # Proportionality constant for contact line motion
# theta_s = 30 # Equilibrium contact angle (degrees)
st_list = [42e-3, 65.6e-3, 63.8e-3]
viscosity_list = [10e-3, 10.5e-3, 58e-3]
theta_s_list = [17.4, 31.2, 32.5]
kappa_list = [2.2e-4, 1.9e-4, 5.2e-4]
L = 24e-3

folder = r"G:\My Drive\Research projects\WPM\Data\Simulation\real_cl"

for mu, sigma, kappa, theta_s in zip(viscosity_list, st_list, kappa_list, theta_s_list):
    for h0 in h0_list:
        # print the file name
        filename = f'mu_{mu:.2e}_sigma_{sigma:.2e}_h0_{h0:.2e}_L_{L:.2e}.csv'
        print(filename)
        # Run the simulation
        fileDir = os.path.join(folder, filename)
        os.system(f'python dimple_simulation.py \"{fileDir}\" --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e} -X {L:.2e} -T 200 -s 0.1')