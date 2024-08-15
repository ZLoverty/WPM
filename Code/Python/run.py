import os
import numpy as np

area_list = np.linspace(2e-4, 10e-4, 5)
Pi0_list = np.linspace(-10, -40, 5)
h0_list = np.linspace(2e-4, 3e-4, 20)
kappa = 1.2e-7    # Proportionality constant for contact line motion
theta_s = np.deg2rad(50) # Equilibrium contact angle (degrees)

folder = r"E:\WPM\Simulation\Scan_initial_thickness"

for area in area_list :
    for Pi0 in Pi0_list:
        for h0 in h0_list:
            # print the file name
            print(f'area_{area:.1e}_Pi0_{Pi0:.1f}_h0_{h0:.2e}.csv')
            # Run the simulation
            filename = os.path.join(folder, f'area_{area:.1e}_Pi0_{Pi0:.1f}_h0_{h0:.2e}.csv')
            os.system(f'python dimple_simulation.py {filename} -a {area:.1e} --kappa {kappa:.1e} --Pi0 {Pi0:.1f} --theta_s {theta_s:.1f} --h0 {h0:.2e}')