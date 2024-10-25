---
date: 2024-10-25
title: pressure with hydrostatics
---

# Pressure with hydrostatics

In the previous model, we use Young-Laplace equation to determine the pressure in a thin fluid film:

$$
p = -\sigma\frac{\partial^2 h}{\partial x^2}.
$$

This formulation works fine for the old model, because in the old model the entire liquid film is thin enough so that hydrostatic pressure is negligible. 

However, in the new model, contact line rise is the driving force for the flow towards the meniscus. The contact line can rise up to a few millimeters. This length is comparable to capillary length $l_c=\sqrt{\sigma/\rho g}$, which means gravity effect is no longer negligible. Actually, if we do not consider hydrostatics in the pressure, the contact line can go infinitely high to approach a $0^\circ$ contact angle, which is unphysical. 

In the old model, we have hydrostatic pressure to balance the surface tension induced rise in the vertical pores, so that the pores do not suck in fluid constantly. Similarly, in the new model, we also need to balance the driving force of surface tension by hydrostatics. 

Considering both points, we need to include hydrostatic pressure into our pressure model:

$$
p = -\sigma\frac{\partial^2 h}{\partial x^2} + \rho g h.
$$

Compare the surface evolutions predicted by the model with / without hydrostatic pressure, we can see that including hydrostatic pressure prevents dimple formation at large $h_0$, while excluding hydrostatic pressure leads to dimple formation in pretty much all $h_0$. A comparison is shown below. We observe that for $h_0=0.2$ mm, the model without hydrostatics breaks down. This is likely due to the constantly large suction at the meniscus, which leads to unphysically large dimple or negative surface height, which fails the solver. In contrast, the model with hydrostatics remains stable. When comparing the two models for thicker films, we also notice that without hydrostatics, the dimple is very persistant regardless of film thickness. This is again due to the fact that there is no balance mechanism for the surface tension suction. By including hydrostatic pressure, the result is closer to experimental observation, where a dimple forms initially and then gets smoothed out. 

<img src="/assets/images/2024/10/include-hydrostatics.png" width=700px>


