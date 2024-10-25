---
date: 2024-10-22
title: new sucking mechanism
---

# New sucking mechanism

This note describes a new possible mechanism for the beet slice to suck liquid. 

## Problem with the old pore model -- too high pressure

In [a previous note](2024-08-13-dimple-simulation.md), we model the suction by the capillary action in the well-like vertical pores. The model yielded nice dimple evolution results, which resembled that observed in experiment. However, a key issue is not resolved: the capillary pressure induced by well-like pores is much larger than the negative pressure that I used in the simulation. I found the capillary pressure by looking up the size of possible pores of beet on [a website](https://www.nottingham.ac.uk/hiddenhalf/crop/sugar-beet.aspx), which is $r\approx 25\;\mu\mathrm{m}$. By assuming a equilibrium contact angle $\theta_s\approx 50^\circ$, we get the capillary pressure

$$
\Pi_0 = \frac{2\pi r \sigma\cos\theta_s}{\pi r^2} \approx 2000\;\mathrm{Pa},
$$

where $\sigma=42\;\mathrm{mN/m}$ is the surface tension of the beet juice. If we apply this as the negative pressure at the suction boundary, our simulation diverges very quickly and no meaningful results are obtained. However, when we lower the negative pressure to the order of $O(10)\;\mathrm{Pa}$, the simulation starts to be stable and generates nice dimple profiles. The problematic pore model is illustrated below.

<img src="/assets/images/2024/10/problematic-pore-model.png" width=500px>

## New mechanism -- wetting

After discussing with other group members, a new sucking mechanism -- wetting -- seems to be a better model. The idea is that the suction in the thin film is due to the movement of the contact line between the liquid and the beet. It typically moves up, which draws fluid from the thin film to fill up the vacancy. This produces a similar effect as the negative pressure, but is potentially weaker than the capillary action of a $r=25\;\mu\mathrm{m}$ tube.

To prove the concept, we need to know where the contact line is on the beet side. Unfortunately, our scan technique fails to resolve the surface profile near the contact line, due to the steep slope. In the picture below, I show a typical scan, where a gap between the film and the beet can be seen. Before the measurement breaks down at the gap, we always get a curving up, which provides a hint of where the contact line is. We can extrapolate the curving up part to intersect with the beet side to get a rough estimate of the contact line location. 

<img src="/assets/images/2024/10/extrapolation.png" width=500px> 

## Observe the contact line in experiment

Alternatively, we can image the contact line directly with a camera to see how it moves over time. The result is shown in the image sequence below. 

<img src="/assets/images/2024/10/surface-direct-image.png" width=700px>

A simple gradient detector helps to extract the surface profile, as shown below. A few observations can be noted:

1. The contact angle is very small;
2. The contact line reaches equilibrium very quickly (within 0.2 s);
3. The liquid thickness continues to decrease after the contact line reaches equilibrium, suggesting that there is another suction mechanism in addition to the immediate contact line rise. I thick this could be caused by the contact line around the beet;
4. After the initial rise, the contact line also goes down a little bit, in accordance with the whole surface thickness decrease.

<img src="/assets/images/2024/10/extract-surface-profiles.png" width=700px>    

During the rise of the contact line, the volume of liquid at the meniscus increases. This requires some fluid flow from the thin film to the meniscus. The result of this action is: when the contact line reaches equilibrium, the fraction of liquid near the beet is increased and that far away from the beet is decreased. This is consistent with our observation in experiment. 

## Estimate the negative pressure 

The flow caused by the rising contact line can also be interpreted by the increase of local curvature at the meniscus, as illustrated below. This high curvature creates a low pressure according to Young-Laplace equation, which drives liquid from the bulk flim to the meniscus. 

<img src="/assets/images/2024/10/contact-line-induce-curvature.png" width=350px>

This is the new mechanism: the beet juice wets the beet surface very well. When forming a meniscus, it causes some amount of flow from the bulk film to the meniscus. For the bulk film, this is as if there is a suction force towards the beet, which can cause the whole film to get thinner, and possibly induce the formation of a dimple.

The negative pressure induced by this new mechanism can be estimated. To do that, we start by looking at a well developed meniscus shown below, to see how much contact line rise is caused by the surface tension. If we look at one point under the meniscus on the $x$-axis, the pressure there is balanced with the bulk surface, so $p=p_0$. From another point of view, where we look from the liquid surface down to this point, we can write the pressure as the net pressure of surface baseline $p_0$, hydrostatic $\rho gy$ and curvature induced pressure $-\sigma\kappa$. Essentially, the surface tension induced pressure is balanced by hydrostatic pressure:

$$
\rho g y = \sigma\kappa,
$$

where $\sigma$ is the surface tension of the liquid and $\kappa$ is the local curvature of the liquid surface. The curvature is defined as the change of the orientation of the tangential vector per unit arc length of the curve:

$$
\kappa = \frac{\mathrm{d}\theta}{\mathrm{d}s}.
$$

Using geometrical relation, we can get

$$
\kappa = \frac{y''}{\left( 1+y'^2 \right)^{3/2}}.
$$

![picture 6](/assets/images/2024/10/curvature.png)  

We can plug the curvature expression in the pressure balance to obtain

$$
\rho g y = \sigma \frac{y''}{\left( 1+y'^2 \right)^{3/2}},
$$

from which we can solve the capillary rise $h_0=y(x=0)$

$$
h_0^2 = \frac{\sigma}{\rho g}(1-\sin\theta_0).
$$

In this analysis, a capillary length scale $l_c=\sqrt{\sigma/\rho g}$ arises, characterizing the capillary rise height of the meniscus. The horizontal span $l_x$ must be on the same length scale as the capillary rise $l_y$, because if $l_x \ll l_y$ or $l_x \gg l_y$, the curvature in the meniscus is too large to be stable. The two unlikely meniscus shapes are sketched above. 

The capillary rise is a balance between surface tension at the contact line and the gravity of the whole meniscus. For a 1D thin liquid film, this balance can be written as 

$$
\frac{\sigma}{l_x}  = \rho g l_y.
$$

The LHS $\sigma/l_x$ can be interpreted as the negative pressure that drives fluid to the meniscus. And this negative pressure can be eventually balanced by the hydrostatic pressure. 

Now we put in numbers and estimate the scale of this pressure. Take the property of beet juice, $\sigma=42\;\mathrm{mN/m}$, $l_x=\sqrt{\sigma/\rho g}\approx 2\;\mathrm{mm}$, the negative pressure caused by surface tension can be estimated as 

$$
\Pi_0 = \frac{\sigma}{l_x} = 21\;\mathrm{Pa}.
$$

Considering that in my previous simulation I've been using $\Pi_0\in[10, 40]$ Pa, which gives reasonable results, this estimate is encouraging evidence that the meniscus contact line rise is responsible for the dimple formation. 

## Contact line velocity

Previously, I did not take the contact line velocity very seriously because it was not the main driving force of the flow. Virtually, I can put any small number there and the resulting surface evolution won't be too off. Now that we are employing the new mechanism, it is important to get the contact line velocity correctly. In previous simulations, we use the Hoffman-de Gennes equation to get contact line velocity

$$
U_{cl} = \frac{\sigma\kappa}{\mu}\theta(\theta^2-\theta_s^2),
$$

where I use $\theta_s=50^\circ$ and $\kappa=10^{-7}$. At $\theta=90^\circ$, the velocity of contact line $U_{cl}\approx 1\;\mu\mathrm{m/s}$. We now have an experimental measurement of $U_{cl}$. Roughly, the contact line rises 2 mm within 0.1 second, giving a velocity $U_{cl}=20\;\mathrm{mm/s}$, 20,000 times of the value in my previous model... I remember I chose a small contact line velocity in previous model to avoid rupturing the dimple. This makes sense because if I set contact line velocity too high, I effectively increase the suction pressure. 

With the new measurement, we can estimate $\kappa$ again. The steady state contact angle is $\theta_s\approx 30^\circ$. We start from $\theta=90^\circ$ and end up with $\theta=30^\circ$, so we use $\theta=60^\circ$ as the intermediate angle for estimate. This gives

$$
\kappa = \frac{\mu U_{cl}}{\sigma\theta(\theta^2-\theta_s^2)}\approx 0.05,
$$

which agrees okay with $\kappa=0.013$ from Hoffman 1975. This parameter will be used in the new numerical simulation.

