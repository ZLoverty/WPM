---
date: 2024-10-25
title: redistribute mass
---

# Redistribute mass

New mechanism introduces new problems. Previously, we had a negative pressure at the left boundary and a very slow prescribed motion of contact line at the left boundary. The prescribed motion is so slow, that the mass coming to the left boundary is essentially lost. In other words, mass is not conserved in the old model. We were happy with this because liquid absorption by the boundary was exactly the result we looked for. With the new mechanism, where contact line motion becomes the source of negative pressure, we assume mass conservation throughout the whole process. This requires special considerations on how to compensate for the mass change caused by the contact line motion, in order to conserve mass. In this note, we summarize the attempts to conserve mass.

## 1 Redistribute to second point

We can compensate the mass increase at contact line by decreasing the second grid point next to the contact line. In the simulation code, this looks like:

```python
if dhdt.sum() != 0:
    dhdt[1] -= dhdt.sum()
```

This strategy works for large initial thickness $h_0$ but breaks down for small $h_0$. Below are a few tests for $h_0\in [0.36, 1]\;\mathrm{mm}$. 

<img src="/assets/images/2024/10/conserve-with-second-point.png" width=700px> 

No curve is generated for even smaller $h_0$. A closer look at the $h_0=0.36\;\mathrm{mm}$ case suggests that the second point for small $h_0$ cases might go below 0, causing the computation to break down. 

## 2 Redistribute to all points

To avoid the second point being to low, I can redistribute the mass change to all grid points in the domain. In the simulation code, this looks like:

```python
if dhdt.sum() != 0:
        dhdt[1:-1] -= dhdt.sum() / (N - 2)
```

Similarly, no curve is generated for $h_0=0.15$ mm. But starting from $h_0=0.36$ mm, the all-point strategy gives better result. The entire time span is covered.

![picture 1](/assets/images/2024/10/conserve-with-all-points.png)  

I therefore adopt the all-point approach. 