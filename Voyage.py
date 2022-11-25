from vpython import *

#objects

#earth = sphere(pos=vector(0,0,0), radius = 6.4e6, color=color.blue)
moon = sphere(pos=vector(4.0e8,0,0), radius = 1.75e7 , color=color.yellow)
craft = sphere(pos=vector(-6.4e6+5000000,0,0),make_trail = True, radius = 1.0e7, color=color.blue)
craft.trail = curve(color=color.white)


#constants
G = 6.67e-11
#earth.M = 6.0e24
moon.M = 7.0e22
craft.M = 150e3
craft.v = vector(0,10,0)
#r = (1/(1-((craft.v)/(3 * 10e8))e2)) #gamma
craft.p =craft.M * (craft.v)

t = 0
dt = 30
#scene.autoscale = 0

#Calculations

while t<100:
    rate(30000)
    R_moon = craft.pos - moon.pos
    #R_earth = craft.pos - earth.pos
    
    F = -G*((moon.M)*(craft.M)*R_moon/mag(R_moon)**3)
    #F = - G*((earth.M)*(craft.M)*R_earth/mag(R_earth)**3)
    craft.p = craft.p+F*dt
    craft.pos = craft.pos + (craft.p/craft.M) *(dt)



    #craft.V = craft.V + (F/craft.M)*(t+dt)
    
