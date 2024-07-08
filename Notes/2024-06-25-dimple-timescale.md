---
date: Jun 25, 2024
---

# Dimple time scale

The surface profile of the thin liquid film with a dimple is shown in the sketch below.

![picture 0](/assets/images/2024/06/dimple-sketch.png)  

The dimple formed in a thin layer of liquid around a porous material is unstable. Surface-tension-induced pressure gradient has the tendency to smooth it out. However, whether this tendency will eventually smooth out the dimple or not depends on the competition between the surface tension induced pressure gradient and the pressure gradient required to drive the lubrication flow in the thin film. This competition can be characterized by capillary number $Ca$:

$$
Ca = \frac{\Delta P_l}{\Delta P_s}, \tag{1}
$$

where $\Delta P_l$ and $\Delta P_s$ are the lubrication flow pressure and the surface tension pressure, respectively. The scale of $\Delta P_l$ can be obtained from the NS equation under lubrication approximation

$$
-\frac{\partial p}{\partial x} + \eta \frac{\partial ^2 v_x}{\partial y^2} = 0, \tag{2}
$$

consider thin film, where the scale of $y$ is much smaller than the scale of $x$, we can nondimensionalize the equation using $\tilde p = p/p_0$, $\tilde x=x/L$, $\tilde v_x = v_x / U$, $\tilde y = y/h$:

$$
-\frac{p_0}{L}\frac{\partial \tilde p}{\partial \tilde x} + \frac{\eta U}{h^2} \frac{\partial ^2 \tilde v_x}{\partial \tilde y^2} = 0, \tag{3}
$$

which gives us the scale of $\Delta P_l$:

$$
\Delta P_l \sim p_0 \sim \frac{\eta U L}{h^2}. \tag{4}
$$

The scale of the surface tension induce pressure drop can be inferred from Young-Laplace equation:

$$
\Delta P = \gamma (\frac{1}{R_1} + \frac{1}{R_2}). \tag{5}
$$

If we postulate that the radius of curvature at the dimple is on the order of the film length $L$, we have:

$$
\Delta P_s \sim \frac{\gamma}{L}. \tag{6}
$$

If we plug Eqs. (4) and (6) to Eq. (1), we get the capillary number

$$
Ca = \frac{\eta U}{\gamma} \left( \frac{L}{h} \right) ^2. \tag{7}
$$

Let $U=L/\tau$, and reorganize Eq. (7), we can see how the characteristic time scale depends on the film thickness $h$:

$$
\tau = \frac{\eta L^3}{Ca\cdot \gamma} \frac{1}{h^2}. \tag{8}
$$

We plot this $\tau$-$h$ relation at various $Ca$ below.

![picture 0](/assets/images/2024/07/dimple%20time%20scale%20depending%20on%20film%20thickness.png)  


## Critical film thickness

Alternatively, we can fix the time scale and seek for a critical film thickness.

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


