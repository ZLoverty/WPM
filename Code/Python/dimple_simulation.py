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

# free parameters
    -k, --kappa : Proportionality constant for contact line motion, default to 0.005
    -P, --Pi0 : Initial pressure at the left boundary (Pa), default to -10
    -t, --theta_s : Equilibrium contact angle (degrees), default to 70
    -a, --pore_area : Area of the pores (m^2), default to 1.0e-3

Example
-------

python dimple_simulation.py E:\WPM\Simulation\Scan_free_params\kappa_1.0e-06_Pi0_0.0_theta_s_0.0.csv --kappa 1.0e-06 --Pi0 0.0 --theta_s 0.0


Edit
----
Aug 14, 2024: Initial commit.
Aug 15, 2024: (i) Edit the docstring to show optional arguments more accurately. (ii) Prevent the increase of total volume due to contact line movement.
Oct 24, 2024: Change the model from micro-pore driven to meniscus rise driven.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import os
import argparse
import pdb
import pandas as pd

# Read constants from command line
parser = argparse.ArgumentParser(description='Dimple simulation')
parser.add_argument('save_file', type=str, help='File to save the solution')
# free parameters
parser.add_argument('-k', '--kappa', type=float, default=0.005, help='Proportionality constant for contact line motion')
parser.add_argument('-P', '--Pi0', type=float, default=-10, help='Initial pressure at the left boundary (Pa)')
parser.add_argument('-t', '--theta_s', type=float, default=30, help='Equilibrium contact angle (degrees)')
parser.add_argument('-a', '--pore_area', type=float, default=1.0e-3, help='Area of the pores (m^2)')
# physical consts
parser.add_argument('--mu', type=float, default=1e-2, help='Viscosity, Pa s')
parser.add_argument('--g', type=float, default=9.8, help='Gravitational acceleration, m/s^2')
parser.add_argument('--sigma', type=float, default=42e-3, help='Surface tension, N/m')
parser.add_argument('--rho', type=float, default=997, help='Density of water, kg/m^3')
# simulation parameters
parser.add_argument('-T', '--time', type=float, default=100, help='Total simulation time (s)')
parser.add_argument('-X', '--X', type=float, default=1e-2, help='Size of the domain (m)')
parser.add_argument('-N', '--number', type=int, default=100, help='Number of radial grid points')
parser.add_argument('-s', '--save_time', type=float, default=.1, help='time interval between each save')
# initial condition
parser.add_argument('--h0', type=float, default=2e-4, help='Initial film thickness profile')
args = parser.parse_args()

# Read constants from command line
# free parameters
kappa = args.kappa    # Proportionality constant for contact line motion
Pi0 = args.Pi0   # Initial pressure at the left boundary (Pa)
theta_s = np.deg2rad(args.theta_s) # Equilibrium contact angle (degrees)
pore_area = args.pore_area # Area of the pores (m^2)

# Physical
sigma = args.sigma  # Surface tension (N/m)
mu = args.mu    # Viscosity (Pa.s)
rho = args.rho     # Density of water (kg/m^3)
g = args.g       # Gravitational acceleration (m/s^2)

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

def film_drainage(t, y, x, X, rho, g, mu, sigma, theta_s):

    h = y
    
    dx = (x[2:] - x[:-2]) / 2
    
    p = YL_equation(h, x, sigma)
    
    # Reynolds equation
    dhdt = np.zeros(h.shape)
    h3 =  h**3
    dhdt[1:-1] = 1 / (12 * mu) * ((h3[2:] - h3[:-2]) * (p[2:] - p[:-2]) + 4 * h3[1:-1] * (p[2:] - 2 * p[1:-1] + p[:-2])) / dx**2

    # boundary conditions
    U_cl = contact_line_velocity(h, x, sigma, mu, theta_s, kappa=kappa)
    dhdt[0] = U_cl

    # conserve mass
    if dhdt.sum() != 0:
        dhdt[1] -= dhdt.sum() 
    
    return dhdt

def YL_equation(h, x, sigma):

    # Young-Laplace equation
    dx = (x[2:] - x[:-2]) / 2
    dh = (h[2:] - h[:-2]) / dx / 2
    d2h = (h[2:] - 2 * h[1:-1] + h[:-2]) / dx**2
    p = np.zeros_like(h)
    p[1:-1] = - sigma * (1 + dh**2)**(-3/2) * d2h #+ rho * g * h[1:-1]
    # p[1:-1] = - sigma * d2h
    # Boundary conditions
    # p[0] =  p_left(h, x, V0, Pi0, pore_area)
    p[0] = p[1]
    p[-1] = p[-2]
    return p

def contact_line_velocity(h, x, sigma, mu, theta_s, kappa=1e-7):
    """
    The contact line motion model of Kim et al. (2017)
    """
    theta = compute_contact_angle_0(h, x)
    U_cl = kappa / mu * sigma * theta * (theta**2 - theta_s**2)
    return U_cl

def compute_contact_angle_0(h, x):
    """
    Calculate the contact angle based on the film thickness profile
    """
    dh = h[1] - h[0]
    dx = x[1] - x[0]

    if dh == 0:
        return np.pi / 2
    else:
        angle = - np.arctan(dx / dh)
        if angle < 0:
            angle += np.pi
        return angle

def p_left(h, x, V0, Pi0, pore_area):
    """
    Calculate the pressure at the left boundary
    """
    # Calculate the total volume of liquid in the domain
    V = np.trapz(h, x)

    # Calculate the pressure at the left boundary
    p = Pi0 + rho * g * (V0 - V) / pore_area
    return p

# Solve the PDE using solve_ivp with the BDF method
nSave = int(T / save_time)
t_eval = np.linspace(0, T, nSave)
solution = solve_ivp(film_drainage, [0, T], h, method='BDF', t_eval=t_eval, args=(x, X, rho, g, mu, sigma, theta_s), atol=1e-6, rtol=1e-6)  # BDF method is suitable for stiff problems

# create save_folder
save_folder = os.path.dirname(args.save_file)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Save the solution in txt file, index name x
data = pd.DataFrame(data=solution.y*1e3, index=x*1e3, columns=solution.t)
data.index.name = 'x'
data.to_csv(args.save_file)
