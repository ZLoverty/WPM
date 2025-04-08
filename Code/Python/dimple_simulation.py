"""
dimple_simulation.py
====================

Description
-----------

This script simulates the evolution of the dimple formation process in a thin liquid film next to a porous material. The inspiration is the fringe around a beet slice.  

Syntax
------

python dimple_simulation.py save_file [optional arguments]

save_file: the folder to save all outputs

optional arguments:
# initial state
    --h0 : Initial film thickness, default to 2e-4

# simulation parameters
    -T, --time : total time of the simulation (s), default to 100
    -X, --X : size of the domain (m), default to 1e-2
    -N, --number : number of spatial discretization, default to 100
    -s, --save_time : Save the states every save_time (s), default to .1

# physical consts
    --mu : viscosity, Pa s, default to 1e-2
    --g : gravitational acceleration, m/s^2, default to 9.8
    --sigma : surface tension, N/m, default to 42e-3
    --rho : density of water, kg/m^3, default to 997
    -k, --kappa : Proportionality constant for contact line motion, default to 0.005
    -t, --theta_s : Equilibrium contact angle (degrees), default to 70

Edit
----
Aug 14, 2024: Initial commit.
Aug 15, 2024: (i) Edit the docstring to show optional arguments more accurately. (ii) Prevent the increase of total volume due to contact line movement.
Oct 24, 2024: Change the model from micro-pore driven to meniscus rise driven.
Nov 05, 2024: (i) Remove unused free parameters. (ii) Convert save_file to absolute path. (iii) Add custom boundary conditions to enable different boundary conditions using the same code.
Apr 03, 2025: Change default liquid properties to beet juice properties.
Apr 08, 2025: (i) Simplify the code: fix BC as Neumann; (ii) Use operators and sparse matrices for computing derivatives; (iii) Remove redundant arguments.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import os
import argparse
import pdb
import pandas as pd
from scipy.sparse import diags, kron, identity

# Read constants from command line
parser = argparse.ArgumentParser(description='Dimple simulation')
parser.add_argument('save_file', type=str, help='File to save the solution')

# physical consts
parser.add_argument('--mu', type=float, default=1e-2, help='Viscosity, Pa s')
parser.add_argument('--g', type=float, default=9.8, help='Gravitational acceleration, m/s^2')
parser.add_argument('--sigma', type=float, default=42e-3, help='Surface tension, N/m')
parser.add_argument('--rho', type=float, default=997, help='Density of water, kg/m^3')
parser.add_argument('-k', '--kappa', type=float, default=2.2e-4, help='Proportionality constant for contact line motion')
parser.add_argument('-t', '--theta_s', type=float, default=17.4, help='Equilibrium contact angle (degrees)')

# simulation parameters
parser.add_argument('-T', '--time', type=float, default=200, help='Total simulation time (s)')
parser.add_argument('-X', '--X', type=float, default=24e-3, help='Size of the domain (m)')
parser.add_argument('-N', '--number', type=int, default=200, help='Number of radial grid points')
parser.add_argument('-s', '--save_time', type=float, default=.1, help='time interval between each save')
# parser.add_argument('--bc', type=str, default=None, help='The path to the json file that specifies the boundary conditions.')

# initial condition
parser.add_argument('--h0', type=float, default=2e-4, help='Initial film thickness profile')
args = parser.parse_args()

# Read constants from command line
save_file = os.path.abspath(args.save_file)

# # boundary conditions
# if args.bc is not None:
#     import json
#     with open(args.bc) as f:
#         bc = json.load(f)
#     print(bc)
#     p_left = bc["p_left"]
#     p_right = bc["p_right"]
# else:
#     p_left = {"type": "Neumann", "value": 0.0}
#     p_right = {"type": "Neumann", "value": 0.0}

# Physical
sigma = args.sigma  # Surface tension (N/m)
mu = args.mu    # Viscosity (Pa.s)
rho = args.rho     # Density of water (kg/m^3)
g = args.g       # Gravitational acceleration (m/s^2)
kappa = args.kappa    # Proportionality constant for contact line motion
theta_s = np.deg2rad(args.theta_s) # Equilibrium contact angle (degrees)

# simulation
T = args.time  # Total simulation time (s)
X = args.X        # Radius of the domain (m)
N = args.number     # Number of radial grid points
x = np.linspace(0, X, N)  # x coordinate
save_time = args.save_time  # time interval between each save

# Initial condition
h = np.zeros_like(x)  # Initial film thickness profile
h[:-1] = args.h0 # Initial film thickness profile

# pre-simulation calculation
V0 = np.trapz(h, x)

dx = x[1] - x[0]  # Grid spacing
# 1D first derivative operator (2nd order accuracy)
Dx = diags([-1, 1], [-1, 1], shape=(N, N), format='csr')
Dx = Dx / (2*dx)
# 1D second derivative operator (2nd order accuracy)
D2x = diags([1, -2, 1], [-1, 0, 1], shape=(N, N), format='csr')
D2x = D2x / dx**2

def film_drainage(t, y):

    h = y
    
    p = YL_equation(h)
    
    # Reynolds equation
    # h3 =  h**3
    # dhdt[1:-1] = 1 / (12 * mu) * ((h3[2:] - h3[:-2]) * (p[2:] - p[:-2]) + 4 * h3[1:-1] * (p[2:] - 2 * p[1:-1] + p[:-2])) / dx**2 
    dhdt = 1 / (3*mu) * ( 3 * h**2 * (Dx @ h) * (Dx @ p) + h**3 * (D2x @ p) )  # 1D Reynolds equation)

    # boundary conditions
    dhdt[0] = contact_line_velocity(h)
    dhdt[-1] = 0

    # conserve mass
    if dhdt.sum() != 0:
        dhdt[1] -= dhdt.sum() 
    
    return dhdt

def YL_equation(h):

    p = - sigma * (1 + (Dx @ h)**2)**(-3/2) * (D2x @ h) + rho * g * h
    # p = - sigma * (D2x @ h) + rho * g * h / 2

    p[0] = p[1]
    p[-1] = p[-2]

    return p

def contact_line_velocity(h):
    """
    The contact line motion model of Kim et al. (2017)
    """
    theta = compute_contact_angle_0(h)
    U_cl = kappa / mu * sigma * theta * (theta**2 - theta_s**2)
    return U_cl

def compute_contact_angle_0(h):
    """
    Calculate the contact angle based on the film thickness profile
    """
    dh = h[1] - h[0]

    if dh == 0:
        return np.pi / 2
    else:
        angle = - np.arctan(dx / dh)
        if angle < 0:
            angle += np.pi
        return angle

# Solve the PDE using solve_ivp with the BDF method
nSave = int(T / save_time)
t_eval = np.linspace(0, T, nSave)
solution = solve_ivp(film_drainage, [0, T], h, method='BDF', t_eval=t_eval, atol=1e-6, rtol=1e-6)  # BDF method is suitable for stiff problems

# create save_folder
save_folder = os.path.dirname(save_file)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Save the solution in txt file, index name x
data = pd.DataFrame(data=solution.y*1e3, index=x*1e3, columns=solution.t)
data.index.name = 'x'
data.to_csv(save_file)
