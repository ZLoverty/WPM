import os
import numpy as np

h0_list = np.linspace(0.15e-3, 1e-3, 5)
# viscosity_list = [1e-3, 10e-3, 15e-3, 1.7e-3, 3.6e-3, 10.5e-3, 58e-3]
# st_list = [72e-3, 42e-3, 23e-3, 68e-3, 66e-3, 64e-3, 62e-3]
mu = 1e-2
sigma = 0.042
kappa = 0.05    # Proportionality constant for contact line motion
theta_s = 30 # Equilibrium contact angle (degrees)
Pi0 = -12
area = 3e-3

folder = r"C:\Users\zl948\Documents\WPM_simulation"

  
for h0 in h0_list:
    # print the file name
    filename = f'mu_{mu:.2e}_sigma_{sigma:.2e}_h0_{h0:.2e}.csv'
    print(filename)
    # Run the simulation
    fileDir = os.path.join(folder, filename)
    os.system(f'python dimple_simulation.py \"{fileDir}\" --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e} -X 2e-2 -T 100')