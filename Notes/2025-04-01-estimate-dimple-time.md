---
date: 2025-04-01
title: estimate dimple time
---

# Estimate dimple time

In our manuscript, we attempted to understand the dimple time data with some scaling argument. The most straightforward way is to get the time scale directly from the lubrication equation and Young-Laplace equation:

$$
\frac{\partial h}{\partial t} = \frac{1}{3\mu} \frac{\partial}{\partial x} \left( h^3 \frac{\partial p}{\partial x} \right),
$$

$$
p = -\sigma \left[1+\left(\frac{\partial h}{\partial x}\right)^2\right]^{-3/2} \frac{\partial^2 h}{\partial x^2} + \rho g h.
$$

If we set $h\sim\mathcal{H}$, $x\sim\mathcal{L}$, $t\sim \tau$, we can get two scalings based on the relative importance between the curvature term and the $\rho g h$ term in the Young-Laplace equation:

$$
\tau = \frac{3\mu\mathcal{L}^4}{\sigma \mathcal{H}^3},
$$

or

$$
\tau = \frac{3\mu \mathcal{L}^2}{\rho g\mathcal{H}^3}.
$$

We define the dimple time $t_\mathrm{dimple}$ as the time when the height ratio between dimple and bulk apex $h_\mathrm{min}/h_\mathrm{max}$ reaches 0.5. This definition bears experimental significance, but the dominating force (curvature or gravity) at $t_\mathrm{dimple}$ is not clear. It is possible that, depending on the initial geometry, both could be the dominating force at dimple time. To gain some insight, we examine our simulated data, focusing on the pressure contribution at the dimple. Below, we plot the gravity and curvature terms separately at the dimple, at dimple time $t_\mathrm{dimple}$, for film length $L$ ranging from 15 to 100 mm ($h_0=0.3$ mm).

<img src="/assets/images/2025/04/pressure-contribution-length.png" width=400px>

Indeed, depending on the film length, at $t_\mathrm{dimple}$, the relative importance between gravity and curvature is different. When the film length is short, curvature term is larger; when the film length is long, gravity term is larger. This can be understood by looking at the dimple evolution in two extreme cases: an extremely short film and an extremely long film. 

<img src="/assets/images/2025/04/short-and-long-evolution.png" width=700px>

In the longer film, the dimple formation barely affect the height of the bulk film. The dimple time criterion is reached by the increase of $h_\mathrm{min}$, whereas $h_\mathrm{max}$ remians almost constant. Dimple time criterion is reached long after the dimple curvature is relaxed, and is driven mainly by gravity. In contrast, in the shorter film, as soon as the dimple forms, the curvature induced suction lowers the bulk film thickness significantly. In this case, the dimple time criterion is reached by lower $h_\mathrm{max}$, while $h_\mathrm{min}$ remains almost constant. The dimple time criterion is reached when the dimple curvature is still relaxing, so the curvature pressure is the primary driving force. 

All our experiments were conducted at $L=24$ mm. Interestingly, at this length, the curvature pressure and the gravity pressure have similar contribution, meaning that we can use either $\tau$ scale to estimate dimple time. Below, we plot half of the gravity time, with the measured dimple time, at various $h_0$. Note that we use $\mathcal{H}\sim h_0$ and $\mathcal{L}\sim L$ here:

$$
\tau_g = \frac{3\mu L^2}{\rho gh_0^3}.
$$

Using the curvature time scale to estimate dimple time is a little trickier, because the length scales $\mathcal{L}$ and $\mathcal{H}$ should be specific to the geometry of the dimple, rather than the initial film. Actually, the deviation of gravity estimate at the small $h_0$ limit is due to the assumption $\mathcal{L}\sim L$ getting worse: the curvature is still not well approximated by $h_0/L^2$, and a better approximation would be $h_0/\lambda^2$, where $\lambda$ is the dimple spreading length. This leads to the following approximation of dimple time based on dimple curvature:

$$
\tau_c = \frac{3\mu\mathcal{L}^4}{\sigma \mathcal{H}^3} \approx \frac{3\mu\lambda^4}{\sigma h_0^3}.
$$

<img src="/assets/images/2025/04/tau-g-and-tau-c.png" width=400px>

As can be seen, in this regime, both $\tau_g$ and $\tau_c$ approximate $t_\mathrm{dimple}$ well. However, it is worth noting that these approximations can be very off when $h_0$ and $L$ are different, and we still need to examine the pressure contribution at $t_\mathrm{dimple}$ to determine whether $\tau_g$ or $\tau_c$ is a better approximation. 

