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

# Parameters
R = 1.0e-3  # Radius of the domain
N = 100  # Number of grid points
T = 1  # Total time
mu = 1.0  # Viscosity
sigma = 1.0  # Surface tension
P0 = -0.1  # Initial negative pressure at the boundary
alpha = 1.0e-2  # Decay rate of the negative pressure
rho = 997  # Density of water
g = 9.8  # Gravitational acceleration

# Initial condition: small perturbation on a flat film
r = np.linspace(R/N, R, N)  # Avoid r = 0 to prevent division by zero
h0 = np.ones_like(r) * 1.0e-3  # Initial film thickness
h0[-90:] = 0

# Compute initial total volume
initial_volume = 2 * np.pi * np.trapz(r * h0, r)

def film_drainage(t, y, r, R, rho, g, mu, sigma, initial_volume):
    h = y
    dr = (r[2:] - r[:-2]) / 2
    p = YL_equation(h, r, sigma, R)
    dhdt = np.zeros(h.shape)
    rh3 = r * h**3
    dhdt[1:-1] = 1 / (12 * mu * r[1:-1]) * ((rh3[2:] - rh3[:-2]) * (p[2:] - p[:-2]) + 4 * rh3[1:-1] * (p[2:] - 2 * p[1:-1] + p[:-2])) / dr**2
    dhdt[-1] = 0
    dhdt[0] = dhdt[1]

    # # Compute current total volume
    # current_volume = 2 * np.pi * np.trapz(r * h, r)
    
    # # Compute volume discrepancy
    # volume_discrepancy = initial_volume - current_volume
    
    # # Distribute the volume discrepancy uniformly
    # if volume_discrepancy > 0:
    #     dhdt[1:-1] += alpha
    # elif volume_discrepancy < 0:
    #     dhdt[1:-1] -= alpha
    
    return dhdt

def YL_equation(h, r, sigma, R):
    dr = (r[2:] - r[:-2]) / 2
    p = np.zeros_like(h)
    p[1:-1] = 2 * sigma / R - sigma / r[1:-1] * (h[2:] - h[:-2]) / dr / 2 - sigma * (h[2:] - 2 * h[1:-1] + h[:-2]) / dr**2
    p[0] = p[1]
    p[-1] = 0
    return p

# Solve the PDE using solve_ivp with the BDF method
t_eval = np.linspace(0, T, 10)
solution = solve_ivp(film_drainage, [0, T], h0, method='BDF', t_eval=t_eval,
                     args=(r, R, rho, g, mu, sigma, initial_volume), rtol=1.0e-6, atol=1.0e-6)

# Debugging information
print(f"Number of time steps in solution: {solution.y.shape[1]}")
print(f"Expected number of time steps: {len(t_eval)}")
print(f"Solver message: {solution.message}")

# Check if the solution has the expected number of time steps
if solution.y.shape[1] != len(t_eval):
    raise ValueError(f"Expected {len(t_eval)} time steps, but got {solution.y.shape[1]}")

# Plot the film thickness profile at multiple time steps on the same axis
time_steps = [0, 2, 4, 6, 8] # Indices of the time steps to visualize
fig, ax = plt.subplots(figsize=(10, 6))

for i in time_steps:
    if i < solution.y.shape[1]:
        ax.plot(r, solution.y[:, i], label=f't = {t_eval[i]:.2f}')
    else:
        ax.plot(r, solution.y[:, -1], label=f't = {t_eval[i]:.2f} (out of bounds)')

ax.set_title('Thin Liquid Film Profile at Multiple Time Steps')
ax.set_xlabel('Radius')
ax.set_ylabel('Film Thickness')
ax.legend()

# Compute the total liquid volume over time
total_volume = 2 * np.pi * np.trapz(np.outer(r, np.ones(len(t_eval))) * solution.y, r, axis=0)

# Plot the total liquid volume over time
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(t_eval, total_volume)
ax2.set_title('Total Liquid Volume Over Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Total Volume')