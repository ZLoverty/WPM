import os
import numpy as np

Pi0_list = np.linspace(-10, -100, 10)
area_list = -4.5e-4 / Pi0_list

h0_list = np.linspace(0.15e-3, 1e-3, 20)
viscosity_list = [1e-3, 10e-3, 15e-3, 1.7e-3, 3.6e-3, 10.5e-3, 58e-3]
st_list = [72e-3, 42e-3, 23e-3, 68e-3, 66e-3, 64e-3, 62e-3]
sigma = 0.042
kappa = 1.2e-7    # Proportionality constant for contact line motion
theta_s = np.deg2rad(50) # Equilibrium contact angle (degrees)
Pi0 = -12
area = 3e-3

folder = r"G:\My Drive\Research projects\WPM\Data\Simulation\realistic_liquid_properties"

for mu, sigma in zip(viscosity_list, st_list):    
    for h0 in h0_list:
        # print the file name
        filename = f'mu_{mu:.2e}_sigma_{sigma:.2e}_h0_{h0:.2e}.csv'
        print(filename)
        # Run the simulation
        fileDir = os.path.join(folder, filename)
        os.system(f'python dimple_simulation.py \"{fileDir}\" -a {area:.2e} -P {Pi0:.2f} --kappa {kappa:.2e}  --theta_s {theta_s:.2e} --h0 {h0:.2e} --mu {mu:.2e} --sigma {sigma:.2e} -X 2e-2 -T 200')