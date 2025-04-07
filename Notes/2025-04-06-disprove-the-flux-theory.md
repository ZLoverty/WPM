---
date: 04-06-2024
title: disprove the flux theory
---

# Disprove the flux theory

## 1. The flux theory

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

By assuming that 

$$
h_d \propto l_d, h_m \propto l_m,
$$

we cancel out all the $l$ terms to arrive at the following proportionality

$$
h_d \propto \frac{\rho g}{\sigma} h_m^3.
$$

The dimple time is governed by the balance between gravity and viscous drag

$$
\rho g \mathcal{H} \sim \frac{\mu\mathcal{L}^2/\tau}{\mathcal{H}^2},
$$

we get a time scale

$$
\tau \sim \frac{\mu \mathcal{L}^2}{\rho g \mathcal{H}^3}.
$$

By choosing $\mathcal{H}\sim h_d$ and $\mathcal{L} \sim L$, the time scale is

$$
\tau \sim \frac{\mu L^2}{\rho g h_d^3}.
$$

By plugging in the proportionality between $h_d$ and $h_m$, we get

$$
\tau \propto \frac{\mu L^2 \sigma^3}{(\rho g)^4 h_m^9}.
$$

Lastly, using the approximation $h_m\sim h_0$, we get 

$$
\tau \propto \frac{\mu\sigma^3}{h_0^9}.
$$

For the $L=24$ mm data, this proportionality can collapse the $t_\mathrm{dimple}$ curves pretty well. 

<img src="/assets/images/2025/04/l24collapse.png" width=400px>

However, as we are going to see later, this -9 scaling does not hold for a different $L$. 

## 2. Different film lengths

Here, we first plot $t_\mathrm{dimple}$ as functions of $h_0$ for various film lengths $L$. Varying scaling exponents, ranging from -6 to -21 are observed. 

<img src="/assets/images/2025/04/different-L-dimple-time.png" width=400px> 

Similarly, the $\sigma^3$ term does not always result in the best collapse. In the following figure, we plot $t_\mathrm{dimple}$ vs. $h_0$ for $L=\{0.02, 0.03, 0.04, 0.05\}$ m, at varying $\sigma$'s. The collapse works well when $L=0.02$ m and $L=0.03$ m, close to our first test $L=24$ mm. However, the collapse becomes off at larger $L$.

<img src="/assets/images/2025/04/collapse-sigma3.png" width=700px>

I found that $\sigma^2$ collapse the curves better at larger $L$. The results are shown below.

<img src="/assets/images/2025/04/collapse-sigma2.png" width=700px>  

This evidence suggests that the $\sigma^3$ is also not universal, but depends on the film length. 

## 3. How to understand this?

My hypothesis is that this scaling relation depends on the total volume of the liquid film. While the contact line rise requires almost a constant volume of liquid to replenish the meniscus, the initial film is sometimes too small to provide all this volume. As a result, the bulk film can shrink significantly in this process, making the viscous drag in the film increase sharply: much higher than $\mu U L / h_0^2$. Instead, the characteristic height of the shrinked film, $h_\mathrm{max}$, should be considered. This idea is illustrated in below. $V_m$ is the volume of liquid that goes into the meniscus. 

<img src="/assets/images/2025/04/meniscus-volume.png" width=400px>  

$V_m$ can be significant when the thin liquid film is very small to start with. I show the surface evolution of thress liquid films below, with the same $h_0=0.3$ mm and different $L\in \{ 16, 24, 100\}$ mm. It can be seen that, when $L$ is small, $h_\mathrm{max}$ decreases quickly over time, and $h_\mathrm{max}\ll h_0$ at $t_\mathrm{dimple}$. In contrast, when $L$ is large, $h_\mathrm{max}$ remains almost constant throughout, so $h_\mathrm{max}\sim h_0$ at $t_\mathrm{dimple}$.

<img src="/assets/images/2025/04/different-lengths.png" width=700px>  

Using a simple volume conservation principle, we can estiamte $h_\mathrm{max}$. 

$$
V_m \approx (h_0 - h_\mathrm{max})L,
$$

$$
h_\mathrm{max} \approx h_0 - \frac{V_m}{L}.
$$

The $t_\mathrm{dimple}$, in most cases, is governed by the balance between gravity and viscous drag, so we can estimate it as 

$$
\tau \sim \frac{\mu L^2}{\rho g h_\mathrm{max}^3}.
$$

Plug in the estimate of $h_\mathrm{max}$, we get

$$
\tau \sim \frac{\mu L^2}{\rho g h_0^3}\left( 1 - \frac{V_m}{h_0L}\right)^{-3}.
$$

