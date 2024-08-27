---
date: 2024-08-27
title: determine free parameters with dimple curvature and surface height
---

# Determine free parameters with dimple curvature and surface height

In the [previous note](2024-08-13-dimple-simulation.md), we obtain a set of free parameter (mainly $\Pi_0=-40$ Pa and $A_p=4$ cm$^2$) by systematically screening free parameters and comparing (visually) the surface profile evolution. While this method gave me some close estimate of the free parameters, they still remain qualitative. 

Recently, I start to compare experiment with simulation more rigorously, by looking at the dimple curvature and the surface height evolution. I found that although the surface evolutions look similar from experiment to simulation, the exact quantities of dimple curvature and surface height evolution differ. Conceptually, the dimple curvature can reflect how strong the suction is, and the surface height evolution can reflect how much liquid can be held by the pores. Therefore, matching these two features between experiment and simulation may give us better choices of free parameters, and in turn more realistic simulations. 

With the current free parameters ($\Pi_0=-40$ Pa and $A_p=4$ cm$^2$), let's compare a pair of experiment and simulation.

<img src="/assets/images/2024/08/typical-exp-sim-pair.png" width=700px> 

This is clearly off. Can we fix this by choosing better free parameters? In the following section, we test various free parameter sets to explore the possiblities.

## Choose free parameters

Here, we fix the volume loss $V_p$ and vary the distributions of $\Pi_0$ and $A_p$. According to our simple model, the volume loss typically balances the capillary pressure in the pores:

$$
\Pi_0 + \rho g \frac{V_p}{A_p} = 0.
$$

In the thin liquid layer, the volume loss can be measured by the drop in film thickness:

$$
V_p = A_f h_p,
$$

where $A_f=0.01$ m$^2$ is the area of the liquid film (this area considers unit length perpendicular to the paper), and $h_p$ is the height loss of liquid in the film. $h_p$ can be expressed as $h_p=h_0-h_{mean}$, where $h_0$ is the initial thickness and $h_{mean}$ is the mean thickness at the end of an experiment (usually in a quasi-steady state). $h_{mean}$ depends on the capacity of the beet slice, and also depends weakly on the total volume in the film if it is too small for the beet capacity. The experimental relation between $h_p$ and $h_0$ is shown in the plot below.

<img src="/assets/images/2024/08/height-loss.png" width=350>

We can observe from the data that none of the height loss $h_p$ exceeds 0.25 mm. For beet juice, this upper bound is 0.21 mm. At initial thickness smaller than 0.21 mm, $h_p$ is smaller than $h_0$, due to large drag before the capillary pressure is balanced. 

This observation motivates us to model $V_p$ as a constant. Since the $h_p$ for beet juice never exceeds 0.21 mm, we set $V_p$ at

$$
V_p = A_f h_{p,max} = 0.01 \times 0.21 \times 10^{-3} = 2.1\times 10^{-6} \; \mathrm{m^3}.
$$

According to Eq.1, we have

$$
-\Pi_0 A_p = \rho g V_p = 0.021\; \mathrm{kg\;m/s^2} = \mathrm{const}.
$$

Now, $\Pi_0$ and $A_p$ are no longer independent, and we reduce the number of free parameter from 2 to 1. With this constraint, we range $\Pi_0\in[-10, -100]$ and set $A_p$ accordingly to run the numerical simulation. We then compare the results with experimental data, specifically the dimple curvature and surface height evolution. Here, we present a comparison with an experiment where $h_0=0.285$ mm. Note that this is the exact experiment shown in the first figure. The comparisons are shown in the figure below. The lines are simulations of various free parameters, and the red dots are the experiment to be matched. From the left panel, we first notice that even with constant $\Pi_0 A_p$, the evolution of surface height can differ very much. And we also observe that the case where $\Pi_0=-70, A_p=3\times 10^{-4}$ (green curve) matches with experimental data very well, indicating that this is a good free parameter set. The curvature comparison is shown in the right panel. None of the simulation curves shows good agreement with experiment, although the magnitudes roughly matches. We further notice that the agreement between simulation and experiment is better in early times than later. This suggests the possibility that there is a slower mechanism that evolves the surface, which is not included in the current model. This mechanism is likely related to evaporation.

<img src="/assets/images/2024/08/detailed-comparison-height-curvature.png" width=700px> 

With a better choice of free parameters, we now look at the surface profile evolution again. 

<img src="/assets/images/2024/08/new-profile-comparison.png" width=700px>  

Compared with the first figure, this has been improved a lot, in that the new simulation now shows a dimple. However, this comparison is still qualitatively off, mainly due to the shift of the dimple location. Therefore, in the paper we may present a different data with $h_0=0.209$ mm.

<img src="/assets/images/2024/08/another-profile-comparison.png" width=700px>

By choosing the parameters corresponding to the blue curve, we obtain good agreement between simulation and experiment in the surface profile evolution.



