---
date: 2024-10-22
title: new sucking mechanism
---

# New sucking mechanism

This note describes a new possible mechanism for the beet slice to suck liquid. In [a previous note](2024-08-13-dimple-simulation.md), we model the suction by the capillary action in the well-like vertical pores. The model yielded nice dimple evolution results, which resembled that observed in experiment. However, a key issue is not resolved: the capillary pressure induced by well-like pores is much larger than the negative pressure that I used in the simulation. I found the capillary pressure by looking up the size of possible pores of beet on [a website](https://www.nottingham.ac.uk/hiddenhalf/crop/sugar-beet.aspx), which is $r\approx 25\;\mu\mathrm{m}$. By assuming a equilibrium contact angle $\theta_s\approx 50^\circ$, we get the capillary pressure

$$
\Pi_0 = \frac{2\pi r \sigma\cos\theta_s}{\pi r^2} \approx 2000\;\mathrm{Pa},
$$

where $\sigma=42\;\mathrm{mN/m}$ is the surface tension of the beet juice. If we apply this as the negative pressure at the suction boundary, our simulation diverges very quickly and no meaningful results are obtained. However, when we lower the negative pressure to the order of $O(10)\;\mathrm{Pa}$, the simulation starts to be stable and generates nice dimple profiles. The problematic pore model is illustrated below.

<img src="/assets/images/2024/10/problematic-pore-model.png" width=500px>

After discussing with other group members, a new sucking mechanism -- wetting -- seems to be a better model. The idea is that the suction in the thin film is due to the movement of the contact line between the liquid and the beet. It typically moves up, which draws fluid from the thin film to fill up the vacancy. This produces a similar effect as the negative pressure, but is potentially weaker than the capillary action of a $r=25\;\mu\mathrm{m}$ tube.

To prove the concept, we need to know where the contact line is on the beet side. Unfortunately, our scan technique fails to resolve the surface profile near the contact line, due to the steep slope. In the picture below, I show a typical scan, where a gap between the film and the beet can be seen. Before the measurement breaks down at the gap, we always get a curving up, which provides a hint of where the contact line is. We can extrapolate the curving up part to intersect with the beet side to get a rough estimate of the contact line location. 

<img src="/assets/images/2024/10/extrapolation.png" width=500px> 

Alternatively, we can image the contact line directly with a camera to see how it moves over time. 