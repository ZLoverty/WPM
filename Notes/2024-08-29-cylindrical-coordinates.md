---
date: 2024-08-29
title: Cylindrical coordinates
---

# Cylindrical coordinates

An important discrepancy between experiment and simulation is the dome shape. In experiment, the dome is asymmetric and has more mass towards the right. Whereas in simulation, the dome is almost perfectly symmetric. I attempted to explain this fact by the fact that in experiment, when scanning, the surface is still evolving. In all the experimental data, the scans are "backward", that is, going from the beet ($x=0$) to the other end ($x=L$). In this process, if the surface is going down, then the dome would have more mass to the left, contradicting the observation. So evolving surface during scan does not explain the asymmetric shape.

It might be the coordinate system problem, because in cartesian coordinate system, left and right are symmetric. But in cylindrical coordinate system, right side has larger radius, and therefore more total volume. Combined with the liquid surface rising in the pores due to absorbed liquid, this could result in asymmetry in the final surface profile. 

In this note, I explore the surface profile evolution in cylindrical coordinate system. The results are shown below. The profile might be slightly asymmetric, but more mass is on the left, and is different from the experimental observation.

<img src="/assets/images/2024/08/cylindrical-coordinates.png" width=700px>

Another hypothesis is that the asymmetric surface profile is caused by evaporation-driven Marangoni flow. A weak evidence is that water surface profile is less asymmetric than beet juice or vinegar.