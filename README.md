# PHSX815_Week6
Repository for Week 6 for Computational Physics at KU Spring 2023 

## integrate.py
Script to calculate numerical integrals using the trapezoidal rule and Gaussian-Legendre quadrature. In this script, a 5th degree polynomial was chosen as the function to integrate.

### Usage:

` python3 integrate.py [-start -end -step -root]`


`-start` lower limit of integral 


`-end`   upper limit of integral 


`-step`  step width for trapezoidal integral 


`-root`  weights/roots for polynomial in Gaussian-Legendre integral 

## mc_int_ellipse.py
Script to perform Monte Carlo integration. In this case, it is an elliptical funtion with the presumption that it is centered at the origin. 

### Usage:

` python3 mc_int_ellipse.py [-xlow -xhigh -ylow -yhigh -samp ]`


`-xlow ` lower limit of integral in the x-direction


`-xhigh`   upper limit of integral in the y-direction


`-ylow ` lower limit of integral in the y-direction


`-yhigh`   upper limit of integral in the y-direction

`-samp`    number of points to plot
