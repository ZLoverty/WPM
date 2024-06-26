---
date: Jun 25, 2024
---

# Dimple time scale

The dimple formed in a thin layer of liquid around a porous material is unstable. Surface-tension-induced pressure gradient has the tendency to smooth it out. However, when the liquid film is sufficiently thin, the dimple can stay obvious for quite long time. It turns out that, as the film gets thinner, the time scale of the smoothing out increases. In this note, I analyze this time scale.

The surface profile of the thin liquid film is shown in the sketch below. $R_2$ and $R_3$ are the radii of curvature of the thin film, at the dimple and the apex of the bulk film respectively. Due to the difference in the curvature, there is a pressure difference between the dimple and the apex. We assume here that the film is thin enough, so that hydrostatic pressure is negligible (be precise how thin). 

![picture 0](/assets/images/2024/06/dimple-sketch.png)  

According to Young-Laplace equation, the pressure difference can be written as

$$
\Delta P = \gamma \left( \frac{1}{R_3} + \frac{1}{R_2}\right), \tag{1}
$$

where $\gamma$ is the surface tension of the liquid. Take the example of beet juice, the surface tension is measured to be $\gamma = 42.5$ mN/m. The flow rate induced by this pressure gradient can be calculated with lubrication approximation as

$$
Q = \frac{12 h^3}{\eta} \frac{\Delta P}{L}, \tag{2}
$$

where $h$ is the thin film thickness, $\eta$ is the liquid viscosity and $L$ is the distance between the dimple and the apex. 

From the flow rate, we can estimate the time scale of this lubrication flow, by considering the time required to displace all the liquid at flow rate $Q$:

$$
\tau = \frac{V_{total}}{Q} = \frac{hL}{\frac{12 h^3}{\eta} \frac{\Delta P}{L}} = \frac{\eta }{12 \Delta P} \frac{L^2}{h^2}. \tag{3}
$$

Plug Eq. 1 into Eq. 3, we can include the effect from surface tension $\gamma$:

$$
\tau = \frac{\eta }{12 \gamma} \frac{L^2}{h^2} \left( \frac{1}{R_3} + \frac{1}{R_2}\right)^{-1}. \tag{4}
$$

We now use Eq. 4 to estimate a critical film thickness $h$, below which the time $\tau$ is too long to smooth out the dimple. This is exactly why the dimple can be observed as if it is a stable configuration. 

From experimental data, we estimate the radius curvature $R_2\approx 40$ mm and $R_3 \to \infty$. We use water viscosity $\eta = 0.001$ Pa s, $L = 0.04$. For the dimple to look like "stable", we need the time scale to be longer relative to our observation time, say $\tau = 60$ s. With these numbers, we have

$$
h_c = \left[ \frac{\eta }{12 \gamma} \frac{L^2}{\tau} \left( \frac{1}{R_3} + \frac{1}{R_2}\right)^{-1} \right]^{1/2} = 0.018\;\mathrm{mm}.
$$

The order of magnitude agrees with the observed film thickness at the dimple. 


