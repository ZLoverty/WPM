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
R = 1.0  # Radius of the domain
N = 100  # Number of grid points
dr = R / N  # Grid spacing
T = 1.0  # Total time
mu = 1.0  # Viscosity
gamma = 1.0  # Surface tension
P0 = -0.1  # Initial negative pressure at the boundary
alpha = 1.0  # Decay rate of the negative pressure

# Initial condition: small perturbation on a flat film
h0 = np.ones(N) + 0.01 * np.random.randn(N)
r = np.linspace(dr, R, N)  # Avoid r = 0 to prevent division by zero

# Function to compute the first derivative
def first_derivative(f, dr):
    return (np.roll(f, -1) - f) / dr

# Function to compute the second derivative
def second_derivative(f, dr):
    return (np.roll(f, -1) - 2 * f + np.roll(f, 1)) / dr**2

# Function to compute the Laplacian in cylindrical coordinates
def laplacian_cylindrical(f, r, dr):
    d2f_dr2 = second_derivative(f, dr)
    df_dr = first_derivative(f, dr)
    laplacian = np.zeros_like(f)
    laplacian[1:] = (1 / r[1:]) * df_dr[1:] + d2f_dr2[1:]
    laplacian[0] = d2f_dr2[0]  # Handle r = 0 separately
    return laplacian

# Define the ODE system
def thin_film_pde(t, h):
    laplacian_h = laplacian_cylindrical(h, r, dr)
    curvature_term = laplacian_cylindrical(h**3 * laplacian_h, r, dr)
    dhdt = -gamma / (3 * mu) * (1 / r) * first_derivative(r * curvature_term, dr)
    
    # Apply time-dependent negative pressure at the boundary
    P_suction = P0 * np.exp(-alpha * t)
    dhdt[-1] += P_suction / mu
    
    return dhdt

# Solve the PDE using solve_ivp with the BDF method
t_eval = np.linspace(0, T, 100)
solution = solve_ivp(thin_film_pde, [0, T], h0, method='BDF', t_eval=t_eval)

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