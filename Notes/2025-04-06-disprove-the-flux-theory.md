---
date: 04-06-2024
title: disprove the flux theory
---

# Disprove the flux theory

The flux theory is based on the fact that the fluid flux at the dimple and in the bulk film. The velocity at the dimple $v_d$ and at the thickest part $v_m$ are

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

Similarly, we assume the pressure in the bulk film as induced by gravity, giving

$$
\frac{\partial p}{\partial x}\bigg|_m \sim \frac{\rho g h_m}{l_m}.
$$

Plug this into the flux balance, we get

$$
-\frac{\sigma h_d^4}{2\mu l_d^3}  \sim -\frac{\rho g h_m^4}{2\mu l_m}.
$$

To understand these approximations, we first need to define all these characteristic lengths $h_d,l_d,h_m,l_m$. 

- $h_d$: dimple thickness;
- $l_d$: can be calculated from dimple curvature $\kappa = h_d / l_d^2$, $l_d = \sqrt{h_d/\kappa}$;
- $h_m$: film apex height;
- $l_m$: hard to define. Maybe $l_m = L - l_m$.

