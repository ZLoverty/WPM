import os
import numpy as np

area_list = [4e-4]
Pi0_list = [-40]
h0_list = np.linspace(1e-4, 8e-4, 40)
viscosity_list = [10e-3, 15e-3, 1e-3]
st_list = [42e-3, 27e-3, 72e-3]
kappa = 1.2e-7    # Proportionality constant for contact line motion
theta_s = np.deg2rad(50) # Equilibrium contact angle (degrees)

folder = r"C:\Users\liuzy\Documents\WPM_Simulation\mu_sigma"

for area in area_list :
    for Pi0 in Pi0_list:
        for h0 in h0_list:
            for mu, sigma in zip(viscosity_list, st_list):
                # print the file name
                filename = f'mu_{mu:.3f}_sigma_{sigma:.3f}_h0_{h0:.2e}.csv'
                print(filename)
                # Run the simulation
                fileDir = os.path.join(folder, filename)
                os.system(f'python dimple_simulation.py {fileDir} -a {area:.1e} --kappa {kappa:.1e} --Pi0 {Pi0:.1f} --theta_s {theta_s:.1f} --h0 {h0:.2e} --mu {mu:.3f} --sigma {sigma:.3f}')