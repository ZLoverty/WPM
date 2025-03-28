---
date: 2025-03-28
title: dimple thickness depends on initial thickness
---

# Dimple thickness depends on initial thickness

We found in both experiment and simulation that the initial dimple thickness $h_\mathrm{dimple}$ at $t=0.5\;\mathrm{s}$ is correlated with the initial film thickness $h_0$. We do not have a good explanation for it, but according to the data, this dependence seems very robust (see the figure below).

<img src="/assets/images/2025/03/dimple-thickness-initial-thickness.png" width="500px">

We attempt to derive this relation from simple principles. 

<img src="/assets/images/2025/03/illustrate-h.png" width="500px">

The flow velocity at the dimple $v_d$ and at the thickest part $v_m$ are

$$
v_d = \frac{1}{2\mu}\frac{\partial p}{\partial x}\bigg|_d(z^2 - 2h_d z),
$$

$$
v_m = \frac{1}{2\mu}\frac{\partial p}{\partial x}\bigg|_m(z^2 - 2h_m z).
$$

Due to mass conservation, the ratio between the maxima of two velocities should be inversely proportional to the height ratio:

$$
v_d^{max} h_d = v_m^{max} h_m.
$$

Plug the velocity expressions in:

$$
-\frac{h_d^3}{2\mu}\frac{\partial p}{\partial x}\bigg|_d = -\frac{h_m^3}{2\mu}\frac{\partial p}{\partial x}\bigg|_m.
$$

Now, let's impose some approximations. The pressure at the dimple is mainly induced by the surface tension, so we approximate it using Young-Laplace equation, setting $h_d$ as the scale of height and $l_d$ as the scale of $x$, giving

$$
\frac{\partial p}{\partial x}\bigg|_d \sim \sigma\frac{h_d}{l_d^3}.
$$

We also approximate $h_m$ as the initial film thickness $h_0$, $h_m\sim h_0$, which should be pretty accurate for the length of films we work with. Lastly, we approximate the pressure in the bulk film as induced by gravity, giving

$$
\frac{\partial p}{\partial x}\bigg|_m \sim \frac{\rho g h_0}{L}.
$$

Combine the approximations above, we get

$$
\sigma\frac{h_d^4}{l_d^3} \sim \frac{h_0^4 \rho g}{L}.
$$

If we make a crude assumption $h_d\sim l_d$ here, we get

$$
h_d \sim \frac{ \rho g}{\sigma L} h_0^4.
$$

How is this approximation? Let's test with a specific case, where $\sigma=42\;\mathrm{mN/m}$, $\rho=1000\;\mathrm{kg/m^3}$, $g=9.8\;\mathrm{m/s^2}$, $L=24\;\mathrm{mm}$ and $h_0=0.3\;\mathrm{mm}$. With these numbers, we estimate $h_d$ to be

$$
h_d \approx 79 \;\mathrm{nm},
$$

much smaller than expected. Clearly, some assumptions do not hold. Particularly, $h_d\sim l_d$ is problematic. We already know that $l_d$ should be close to capillary length (a few mm), and $h_d$ is typically much smaller than $h_0$, on the order of $0.01\;\mathrm{mm}$, so this approximation introduces huge error. 

What if we only claim the proportionality between $h_d$ and $l_d$? In some cases, this is probably close. But it's definitely not always true. Observing from the simulation data, it seems more true for early time, or long films. See two examples below. In the shorter film (left), we observe an increase of $h_d$ during the spreading, but later on $h_d$ becomes more constant, while keep spreading. In the longer film (right), $h_d$ and $l_d$ seem to be pretty linearly related. 

<img src="/assets/images/2025/03/hd-ld.png" width="700px">

This observation may justify the proportionality $h_d\propto l_d$ at early times. With this proportionality, we can write  

$$
h_d \propto \frac{ \rho g}{\sigma L}h_0^4.
$$