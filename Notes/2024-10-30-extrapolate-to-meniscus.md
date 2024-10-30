---
date: 2024-10-30
title: extrapolate to meniscus
---

# Extrapolate to meniscus

The confocal displacement sensor works great on relatively flat surface. When coming to the meniscus on a vertical wall, however, the steep elevation and the large slope makes detecting reflection challenging. As a result, all our scan data missed the meniscus part, and some meaningless large negative values were given. An example scan data is shown below, where the large negative values caused by the meniscus are annotated. 

<img src="/assets/images/2024/10/large-negative-values.png" width=700px> 

If we zoom in one of the surface scans, we can see the important features, namely the bulk film apex and the dimple. Therefore, we can measure the dimple time based on the scan data unambiguously. The [newly proposed sucking mechanism](2024-10-22-new-sucking-mechanism.md) based on contact line rise makes it desired to have more information on the contact line location. We could [image contact line directly](2024-10-22-new-sucking-mechanism.md), but when the liquid film is very thin ($\sim 0.2$ mm), the resolution of liquid film is too low to resolve any deformation. 

Alternatively, we can extrapolate the surface profile from the correct scan data to the vertical wall. Here, I tried to use polynomial extrapolation, with the data from mid point to the "tip" point. A typical result is shown below. The extrapolated curve looks right qualitatively. First, the contact line is rising constantly. Second, the rising speed is faster at the beginning and slower at the end, consistent with our model. 

<img src="/assets/images/2024/10/extrapolate-data.png" width=500px>

We also checked the mass conservation by looking at the mean surface height over time. A slight increase over time can be observed, which could be attributed to the fitting error. 

<img src="/assets/images/2024/10/check-mass.png" width=700px>

Overall, I think plotting the surface in a coordinate where $x=0$ is the vertical wall is more proper. The old way, where I put $x=0$ at the "tip", can be somewhat misleading. In the revised manuscript, I will do this way, but make it clear that the meniscus part is from extrapolation. 
