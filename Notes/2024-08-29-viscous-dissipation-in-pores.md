---
date: 2024-08-29
title: viscous dissipation in pores
---

# Viscous dissipation in pores

Previously, we used the capillary pressure and the hydrostatic pressure to determine the negative pressure at the $x=0$. We are able to simulate dimple formation with this model, but a problem is that we have to use unrealistically low capillary pressure $\Pi_0$.

<img src="/assets/images/2024/08/model-sketch.png" width=350px>

To be more specific, the pores in the beet slice are no larger than 50 $\mu$m in diameter. Given contact angle $\theta_s=50^\circ$, we estimate the capillary pressure to be 

$$
P_{c} = \frac{2\sigma\cos\theta_s}{r} \approx 2060 \; \mathrm{Pa},
$$

much larger than the pressure we used in simulation. If we use this pressure value, the simulation will collapse in short time, and no dimple formation can be observed.

It turns out that the reason this high pressure leads to trouble in our simulation is because we did not consider viscous dissipation in the pores, which has to exist. When fluid is transported through the pores, it experiences the drag by the walls, and thus requires a pressure drop to sustain its flow motion. This pressure drop would then lead to smaller negative pressure at the $x=0$ boundary, which makes large capillary pressure possible.

In this note, we add this feature to the model and see if it can help incorporate more realistic physical parameters in this model. The pressure boundary condition at $x=0$ would now be

$$
p(x=0) = \Pi_0 + \rho g h_p - h_p \frac{\partial p}{\partial z},
$$

where $h_p = V_p/A_p$ is the liquid height in the pores, $\partial p/\partial z$ is the pressure gradient that causes the flow in the pore. This pressure gradient depends on the flow rate in the pore $q$. The total flow rate $Q$ can be calculated as

$$
Q = -\frac{\partial V}{\partial t},
$$

where $V$ is the total liquid volume in the film. Assuming there are $n$ pores total in the beet slice, then $q = Q / n$. Using the pipe viscous flow model, we can also get the relation between the pressure gradient $\partial p/\partial z$ and the pore flow rate $q$ as

$$
q = -\frac{\pi R_p^4}{8\mu} \frac{\partial p}{\partial z},
$$

where $R_p$ is the pore radius, $\mu$ is the fluid viscosity. Plugging back to the boundary condition, we get

$$
p(x=0) = \Pi_0 + \rho g h_p +  \frac{8\mu q h_p}{\pi R_p^4}.
$$

We notice that in the slow limit when $q=0$, the pressure is still determined by the capillary pressure and hydrostatic pressure. We know already that even we fill up the whole beet slice, the hydrostatic pressure is only about 2.5%, and is insignificant. One possible way to balance the capillary pressure is a sustained flow in the pores. Let's estimate how much this can increase the pressure at $x=0$. Consider a liquid film that covers an area of $A_f=2$ cm$^2$ with initial thickness $h_0=0.2$ mm. Say, within 20 seconds, the whole film is absorbed into the beet. This amounts to a flow rate of $Q=2\times 10^{-9}$ m$^3$/s. Assuming the total pore area is $A_p=0.01$ cm$^2$ and single pore radius is $R_p=25$ $\mu$m, then there are $n=500$ pores in total. The flow rate in each pore is $q=Q/n=4\times 10^{-12}$ m$^3$/s. With $q$, we can compute the pressure gradient in the pore due to the flow:

$$
\frac{\partial p}{\partial z} = -\frac{8\mu q}{\pi R_p^4}=-2.6\times 10^{4} \; \mathrm{Pa/m}.
$$

For fully filled pores, where $h_p=0.005$ m, the pressure drop is 130 Pa. By further decreasing the number of pores, we can achieve a pressure drop that is significant enough for the capillary pressure. However, we note that the flow rate used here is overestimated. In the later part of an experiment, the flow rate is only 1/10 of this estimate, so viscous dissipation is definitely not enough to balance the huge capillary pressure.

Maybe there is just no such pores. Fluid goes underneath the cavities below the beet slice. The cavity underneath the beet slice does not have to be the same scale as the xylem cells, but can be larger, so that it generates a negative pressure on the order of 10-100 Pa. To generate that, typically we need a cavity 100 $\mu$m in diameter. Or the same area but different shape. This is more realistic.