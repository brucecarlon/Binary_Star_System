# <center> Binary Star System Numerical Modelling and Simulation

>This jupyter notebook is presented as report on the modelling of a binary star system using numerical computing. We solve the binary star system equation of motion using ODEINT differential solver from the scipy module

## Description
The binary star system will consist of a G and K class stars. It can be
shown, without loss of generality, that a two-body problem is always evolving in a two-
dimensional orbital plane. The force that drives the motion of the two stars in this model
is the gravitational force.
Therefore, the force of an object of mass M at location (x_M , y_M ) acting on another
object of mass m at location (xm , ym ) is given by the following two formulae (one for each2
coordinate, x and y):

$$ F_x = G \left ( \frac{M \cdot m}{R^2} \right ) \frac{r_x}{R} $$
$$ F_y = G \left ( \frac{M \cdot m}{R^2} \right ) \frac{r_y}{R} $$

where G = 6.67408 × 10−11 m3 kg−1 s−2 is the gravitational constant, R is the distance
between each objects given as:

$$ R = \sqrt{r^2_x + r^2_y} $$
 
and r<sub>x</sub> = x<sub>M</sub> − x<sub>m</sub> and r<sub>y</sub>= y<sub>M</sub> − y<sub>m</sub> , the signed relative positions between the two objects.
The acceleration resulting from this force acting on object m at location (x<sub>m</sub> , y<sub>m</sub> ) is then
given by

$$ a_x = \frac{dv_x}{dt} = G \left ( \frac{M}{R^2} \right ) \frac{r_x}{R} $$

$$ a_y = \frac{dv_y}{dt} = G \left ( \frac{M}{R^2} \right ) \frac{r_y}{R} $$

Integrating equations a<sub>x</sub> and a<sub>y</sub> gives us information on the velocity of the star with mass m which we can use to the change in position given by:

$$ x(t) ≈ x_0 + v_x (t) · \Delta t $$
$$ y(t) ≈ y_0 + v_y (t) · \Delta t $$

derived from $v = \frac{dx}{dt}$

For the purpose of this report we will use the odeint() differential equation solver from the scipy module

## Aim
To compute the forces on the planets as their orbits propogate and establish whether the two stars orbit each other in a stable fashion. we then use data from the orbits to plot a x position vs time graph in order to deduce the period of the orbits.


## Author info
Bruce Mvubele \
[LinkedIn](https://www.linkedin.com/in/bruce-mvubele-494105143/) \
e-mail: cmvubele@gmail.com
