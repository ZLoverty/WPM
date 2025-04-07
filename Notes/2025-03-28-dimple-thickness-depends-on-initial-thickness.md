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

Lastly, we approximate the pressure in the bulk film as induced by gravity, giving

$$
\frac{\partial p}{\partial x}\bigg|_m \sim \frac{\rho g h_m}{l_m}.
$$

Combine the approximations above, we get

$$
\sigma\frac{h_d^4}{l_d^3} \sim \frac{h_m^4 \rho g}{l_m}.
$$

We now make crude assumptions:

$$
h_d \propto l_d,\, h_m \propto l_m.
$$ 

With these, we get

$$
 h_d \propto  \frac{\rho g}{\sigma} h_m^3.
$$

Locally, at the dimple, the surface tension is balanced with the viscous drag, giving

$$
\frac{\sigma h_d}{l_d^2} \sim \frac{\mu l_d /\tau }{h_d^2},
$$

we can approximate the time scale $\tau$ as

$$
\tau \sim \frac{\mu l_d^4}{\sigma h_d^3}.
$$

Using the flux balance, we can construct the proportionality between $\tau$ and $h_m$

What if we only claim the proportionality between $h_d$ and $l_d$? In some cases, this is probably close. But it's definitely not always true. Observing from the simulation data, it seems more true for early time, or long films. See two examples below. In the shorter film (left), we observe an increase of $h_d$ during the spreading, but later on $h_d$ becomes more constant, while keep spreading. In the longer film (right), $h_d$ and $l_d$ seem to be pretty linearly related. 

<img src="/assets/images/2025/03/hd-ld.png" width="700px">

This observation may justify the proportionality $h_d\propto l_d$ at early times. With this proportionality, we can write  

$$
h_d \propto \frac{ \rho g}{\sigma l_m}h_m^4.
$$

I find it difficult to justify the relation between $h_m \propto l_m$ . The only way I can think of right now is to use experimental or simulation data. This is not helpful because that's exactly what we were trying to avoid: using experimental data to justify $h_\mathrm{dimple}\propto h_0^{2.5}$. Since we will have to use experimental data any way, this is not worth pursuing. Instead, we show that the $h_\mathrm{dimple}\propto h_0^{2.5}$ scaling is not sensitive to the choice of the specific time. At early stage of the dimple formation (~1 s), this scaling is robust. We show below the relation between $h_\mathrm{dimple}$ and $h_0$ at two other times $t=0.1$ s and $t=2.0$ s. 

<img src="/assets/images/2025/03/h-h0-different-time.png" width="700px">