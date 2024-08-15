---
date: 2024-08-13
title: dimple simulation
---

# Dimple simulation

I'd like to use Stokes-Reynolds thin film equation to capture the dimple formation in the liquid film around a beet slice. Previously, I successfully applied this model to bubble bouncing, suggesting that the model captures surface motion very well. In the application of dimple, we need to add new features to the model, namely (i) contact angle at the boundary of liquid film, (ii) negative pressure at the contact point of beet.

## 1 Simplest form of Reynolds equation

We start to look at the simplest form of Reynolds equation

$$
\frac{\partial h}{\partial t} = \frac{1}{3\mu x} \left( h^3 \frac{\partial p}{\partial x} \right), 
$$

with pressure determined from Young-Laplace equation

$$
p = -\sigma \frac{\partial^2 h}{\partial x^2}.
$$

The boundary conditions are a pure Dirichlet

$$
h(x=0) = 0,\, h(x=L) = 0, \\
p(x=0)=0, p(x=L) = 0. 
$$

We initialize the system with part of the film thickness $h=0.2$ mm, and the rest being $h=0$ mm. The solution of these equations is shown below:

![picture 0](/assets/images/2024/08/simple_thin_film.png)  

One thing to note is that, even in this simple case, the mass is not perfectly conserved.

Now, change left boundary to -10.

$$
h(x=0) = 0.0002,\, h(x=L) = 0, \\
p(x=0) = -10, p(x=L) = 0. 
$$

![picture 1](/assets/images/2024/08/const%20negative%20boundary%20pressure.png)

This already shows the dimple. However, compared to experiment, this result has two unrealistic features: (i) the left contact line between liquid and beet moves in experiment, while in simulation it is fixed as a boundary condition; (ii) the right contact line between liquid and solid substrate is pinned at a constant position, while in simulation it is allowed to slide. 

## 2 Contact line dynamics

### 2.1 Left side

Let's first modify the model by relaxing the $h(0)=const$ condition. Instead, we will enforce a constant contact angle. This idea follows Kim 2017, where the velocity of a contact line is correlated with its difference from the equilibrium contact angle. Formally:

$$
U_{cl} = \frac{\sigma\kappa}{\mu} \theta (\theta^2 - \theta_s^2),
$$

where $U_{cl}$ is contact line velocity, $\sigma$ is surface tension, $\kappa$ is a coupling parameter that can be determined with experimental data, $\mu$ is viscosity and $\theta_s$ is stationary contact angle. 

$$
\frac{\partial h}{\partial t}(x=0) = U_{cl},\, h(x=L) = 0, \\
p(x=0) = -10, p(x=L) = 0. 
$$

![picture 0](/assets/images/2024/08/moving-contact-line.png)  

This set of boundary conditions gives even better dimple dynamics, especially the **horizontal shift of dimple location**, which resembles the experiment. However, the solution is not stable after a short time. The problem comes from the constant pressure boundary condition `p[-1]=0`. By replacing it with `p[-1]=p[-2]`, the solution gets more stable with moving contact line.

$$
\frac{\partial h}{\partial t}(x=0) = U_{cl},\, h(x=L) = 0, \\
p(x=0) = -10, \frac{\partial p}{\partial x}(x=L) = 0. 
$$

![picture 1](/assets/images/2024/08/smoother-boundary-condition.png)  

### 2.2 Right side

We would like a pinned contact line at the right boundary. It was noticed that by  increasing the initial total liquid volume, and imposing $h=0$ at $x=L$, **we automatically obtained a pinned contact line at the right boundary**. Additional constaints are not required. Hence, we will follow this practice.

![picture 3](/assets/images/2024/08/more-liquid.png)  
 
## 3 Free parameters

### 3.1 $\theta_s$, $\Pi_0$ and $\kappa$

There are a few free parameters in the current model, which we could not determine unambiguously. These include the contact line velocity coefficient $\kappa = 10^{-7}$, boundary negative pressure $p(x=0) = \Pi_0 = -10$ Pa, and the stationary contact angle $\theta_s=70^\circ$. By fine tuning the free parameters, such as $\kappa$ and $\Pi_0$, we can alleviate unphysical scenario such as unconserved mass. For example, too fast contact line velocity results in mass increase in the thin film. It must be unphysical, and we can eliminate it by reducing $\kappa$. In this section, we perform a systematic scan of $\kappa\in[10^{-6}, 10^{-8}$, $\Pi_0\in[0, -20]$ and $\theta_s\in[0, 90]$. 

The physical constants are set as $\sigma=0.072$, $\mu=0.01$ (10x water), $\rho=997$, $g=9.8$, all in SI units. The viscosity $\mu$ has not been measured. We choose 0.01 because it produces results that match experiment better. In the future we can measure.

The simulation will be running $T=100$ s for all cases. The space is $L=1$ cm divided into 100 grid points. Initial condition is chosen to be a flat film of thickness 0.2 mm, except at the right boundary, where $h=0$. The boundaries are modeled as the following:

$$
\frac{\partial h}{\partial t}(x=0) = U_{cl},\, h(x=L) = 0, \\
p(x=0) = -\Pi, \frac{\partial p}{\partial x}(x=L) = 0. 
$$

A selection of simulation results is shown in the figure below. Three big panels are the data at different $\theta_s=0^\circ, 50^\circ, 70^\circ$. Inside each panel, suction pressure $|\Pi_0|$ increases from left to right, contact line velocity coefficient $\kappa$ decreases from top to bottom. The (1) and (2) are selected for a zoom-in view in the bottom panels.

![picture 4](/assets/images/2024/08/free_parameter_scan.png)  

A rough comparison with experimental data suggests that the parameter set in (1), namely $\theta_s=50^\circ$, $\Pi_0=-8.9$ and $\kappa=1.2\times 10^{-7}$ the best free parameter set, particularly because it causes the dimple to displace towards bottom right, an outstanding feature of experimental data. Therefore, $\theta_s=50^\circ$ and $\kappa=1.2\times 10^{-7}$ will be fixed at these values in all future simulations. 

I want to put a hold on fixing the $\Pi_0$ value for the following reasons:
1. The simulation result is more sensistive to the pressure, especially the initial film thickness height where the transition from no-dimple to dimple happens. 
2. In the next section we are going to modify the pressure. Instead of using a constant negative pressure, we are going to model it as time-dependent. So the constant value that works well in the first parameter scan may not be optimal for the new model.

Therefore, let's leave the determination of $\Pi_0$ to the next section.

### 3.2 Decaying suction pressure

As the pores in beet holds more liquid, the liquid-air interface rises, leading to an increase in the pressure at the left boundary of our simulation domain. This effect can be modeled by

$$
\Pi = \Pi_0 + \rho g h_p,
$$

where $h_p$ is the liquid-air interface height in the pores. Given the total volume held by the pores $V_p$ and the cross-section area of the pores $A_p$, we can compute $h_p = V_p / A_p$. Assuming no water is in the beet at the beginning of the simulation, $V_p(t=0) = 0$, we can use the liquid volume reduction in the simulation domain as an estimate of $V_p$

$$
V_p(t) = V_0 - V(t),
$$ 

where $V_0$ is the initial volume and $V(t)$ is the instantaneous volume at time $t$. Now, we have an additional free parameter $A_p$, which also requires a thorough scan to determine a value that matches experiment best. 

In this section, we will scan the combination of initial negative pressure $\Pi_0 \in [-10, -40]$ and the pore cross-section area $A_p\in [2\times 10^{-4}, 10\times 10^{-4}]$. The initial film thickness is set at $h_0=0.2$ mm, close to the experimental crossover thickness. The result is shown in the figure below. 3 sets of parameters look pretty promising, as they show the dimple dynamics very close to experimental observation. They are indicated in the figure by red dashed boxes.

![picture 5](/assets/images/2024/08/scan_area_and_pressure.png)  

In the next section, we are going to vary the initial liquid film thickness, to see which free parameter set can predict the crossover thickness ($\sim 0.2$ mm) best.

### 3.3 Initial film thickness crossover

After the parameter scan of previous section, we land on three candidate parameter sets of $(\Pi_0, A_p)$: $(-40, 4\times 10^{-4}), (-25, 6\times 10^{-4}), (-17.5, 10\times 10^{-4})$. In this section, we want to see which parameter set correctly predict the crossover initial film thickness $h_0$, above which dimple will be smoothed out by surface tension. We examine $h_0 \in [0.2, 0.3]$ (mm). Note that in experiment, the crossover happens at $h_c = 0.208$ mm. The results are shown in the figure below. 

![picture 6](/assets/images/2024/08/scan_initial_thickness.png)  

Qualitatively, all the parameter sets give good results. To be more quantitative, we can look at a characteristic number of each simulation and compare with experiment. Here, we choose to compare the dimple lifetime first. The figure below shows the dimple lifetime measurement for the three parameter sets. The initial film thickness $h_0$ scanned is $[0.2, 0.225, 0.25, 0.275, 0.3]$.

![picture 7](/assets/images/2024/08/dimple_lifetime_measurement.png)  

There are issues with this measurement:

1. The simulation only runs for $T=100$ s, so dimple lifetime beyond 100 s will be cutoff at 100 s, and is thus not accurate. Experiment has the same problem. 
2. 5 points is still a little sparse in the [0.2, 0.3] range. More points would make comparison with experimental data easier. 

Here, we redo the dimple lifetime measurement, sampling 20 initial film thicknesses in the range [0.2, 0.3]. Combining with the 25 free parameter sets, this scan will result in 500 surface evolution data in total. The resulting dimple time $t_{dimple}$ as a function of initial film thickness $h_0$ with various sets of free parameters is shown in the figure below. On top of the simulation result, we also plot the very limited experimental data. Based on the available data, it is difficult to determine a best free parameter set. This analysis also points out that much more experimental data of dimple time is required to inform, as well as to validate the theoretical model. 

![picture 8](/assets/images/2024/08/dimple_time_vs_initial_thickness.png)  


