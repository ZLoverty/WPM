"""
dimple_simulation.py
====================

Description
-----------

This script simulates the evolution of the dimple formation process in a thin liquid film next to a porous material. The inspiration is the fringe around a beet slice.  

Syntax
------

python dimple_simulation.py save_folder [optional arguments]

save_folder: the folder to save all outputs

optional arguments:
# initial state
    -H, --H0 : initial separation (m), default to 1e-3
    -V, --V0 : initial velocity (m/s), default to 0
    -R, --radius : bubble radius (m), default to 5e-4

# simulation parameters
    -T, --time : total time of the simulation (s), default to 0.02
    -N, --number : number of spatial discretization, default to 100
    -s, --save_time : Save the states every save_time (s), default to 1e-4
    --rm : the range of film force integration, the fraction of bubble radius R, default to 0.9
    --load_folder: Folder to load initial state from, default to None.

# physical consts

    --mu : viscosity, Pa s, default to 1e-3
    --g : gravitational acceleration, m/s^2, default to 9.8
    --sigma : surface tension, N/m, default to 72e-3
    --rho : density of water, kg/m^3, default to 997


Edit
----

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define parameters
sigma = 0.072  # Surface tension (N/m)
mu = 0.001    # Viscosity (Pa.s)
T = .1     # Total simulation time (s)
R = 1e-3         # Radius of the domain (m)
dr = 0.01     # Radial step size (m)
N = 100       # Number of radial grid points
rho = 997     # Density of water (kg/m^3)
g = 9.8       # Gravitational acceleration (m/s^2)
r = np.linspace(-R, R, N)  # Radial coordinate
h0 = np.ones_like(r)*1e-4  # Initial film thickness profile
h0[:30] = 0
h0[-30:] = 0

def film_drainage(t, y, r, R, rho, g, mu, sigma):
    
    h = y

    dr = (r[2:] - r[:-2]) / 2
    
    p = YL_equation(h, r, sigma, R)

    dhdt = np.zeros(h.shape)
    rh3 = r * h**3
    dhdt[1:-1] = 1 / (12 * mu * r[1:-1]) * ((rh3[2:] - rh3[:-2]) * (p[2:] - p[:-2]) + 4 * rh3[1:-1] * (p[2:] - 2 * p[1:-1] + p[:-2])) / dr**2
    dhdt[-1] = 0
    dhdt[0] = 0

    return dhdt

def YL_equation(h, r, sigma, R):
    dr = (r[2:] - r[:-2]) / 2
    p = np.zeros_like(h)
    p[1:-1] = 2 * sigma / R - sigma / np.abs(r[1:-1]) * (h[2:] - h[:-2]) / dr / 2 - sigma * (h[2:] - 2 * h[1:-1] + h[:-2]) / dr**2
    p[0] = 0
    p[-1] = 0
    return p

# Solve the PDE using solve_ivp with the BDF method
t_eval = np.linspace(0, T, 100)
solution = solve_ivp(film_drainage, [0, T], h0, method='BDF', t_eval=t_eval, args=(r, R, rho, g, mu, sigma), atol=1e-6, rtol=1e-6)  # BDF method is suitable for stiff problems

# Debugging information
print(f"Number of time steps in solution: {solution.y.shape[1]}")
print(f"Expected number of time steps: {len(t_eval)}")
print(f"Solver message: {solution.message}")

# Check if the solution has the expected number of time steps
if solution.y.shape[1] != len(t_eval):
    raise ValueError(f"Expected {len(t_eval)} time steps, but got {solution.y.shape[1]}")

# Plot the film thickness profile at multiple time steps
time_steps = [0, 25, 50, 75, 99]  # Indices of the time steps to visualize
for i in time_steps:
    plt.plot(r, solution.y[:, i], label=f't={t_eval[i]:.2f}s')
plt.xlabel('Radius (m)')
plt.ylabel('Film thickness (m)')
plt.legend()
plt.title('Settling of a Sessile Drop')
plt.show()