---
date: 2024-08-13
title: dimple simulation
---

# Dimple simulation

I'd like to use Stokes-Reynolds thin film equation to capture the dimple formation in the liquid film around a beet slice. Previously, I successfully applied this model to bubble bouncing, suggesting that the model captures surface motion very well. In the application of dimple, we need to add new features to the model, namely (i) contact angle at the boundary of liquid film, (ii) negative pressure at the contact point of beet.

## Contact line dynamics

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

![picture 1](/assets/images/2024/08/const%20negative%20boundary%20pressure.png)

This already shows the dimple. However, compared to experiment, this result has two unrealistic features: (i) the left contact line between liquid and beet moves in experiment, while in simulation it is fixed as a boundary condition; (ii) the right contact line between liquid and solid substrate is pinned at a constant position, while in simulation it is allowed to slide. 

Let's first modify the model by relaxing the $h(0)=const$ condition. Instead, we will enforce a constant contact angle. This idea follows from Kim 2017, where the velocity of a contact line is correlated with its difference from the equilibrium contact angle. Formally:

$$
U_{cl} = \frac{\sigma\kappa}{\mu} \theta (\theta^2 - \theta_s^2),
$$

where $U_{cl}$ is contact line velocity, $\sigma$ is surface tension, $\kappa$ is a coupling parameter that can be determined with experimental data, $\mu$ is viscosity and $\theta_s$ is stationary contact angle. The best result is shown below:

![picture 0](/assets/images/2024/08/moving-contact-line.png)  

However, running the simulation a little long would result in a very large number at `h[-1]`, despite it is already enforced to be `0` by boundary condition. It turns out that the problem comes from the constant pressure boundary condition `p[-1]=0`. By replacing it with `p[-1]=p[-2]`, the solution can run much longer with moving contact line, as shown below:

![picture 1](/assets/images/2024/08/smoother-boundary-condition.png)  

Modify the initial condition to increase the total liquid amount, results in the following nice dimple profile, resembles the observations in experiment. However, there are two issues: (i) the mass is not conserved. What's worse, the volume can increase due to the moving contact line even if we have a suction force induced by negative pressure at the `x=0` boundary, which is unphysical; (ii)

![picture 2](/assets/images/2024/08/more-lliquid.png)  

Much longer simulation, would the total volume go down eventually?

![picture 3](/assets/images/2024/08/longer-simulation.png)  

The contact line velocity has a free parameter, which may be used for matching the experimental dimple position and lifetime. 

