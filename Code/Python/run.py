import os
import numpy as np

Pi0_list = np.linspace(-1, -100, 10)
area_list = -0.015 / Pi0_list

h0_list = [0.209e-3]
# viscosity_list = [10e-3, 15e-3, 1e-3]
# st_list = [42e-3, 27e-3, 72e-3]
mu = 0.01
sigma = 0.042
kappa = 1.2e-7    # Proportionality constant for contact line motion
theta_s = np.deg2rad(50) # Equilibrium contact angle (degrees)

folder = r"G:\My Drive\Research projects\WPM\Data\Simulation\detail_Pi0_area_small_h0"

for area, Pi0 in zip(area_list, Pi0_list):    
    for h0 in h0_list:
        # print the file name
        filename = f'area_{area:.2e}_Pi0_{Pi0:.2e}_h0_{h0:.2e}.csv'
        print(filename)
        # Run the simulation
        fileDir = os.path.join(folder, filename)
        os.system(f'python dimple_simulation.py \"{fileDir}\" -a {area:.2e} -P {Pi0:.2f} --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e}')