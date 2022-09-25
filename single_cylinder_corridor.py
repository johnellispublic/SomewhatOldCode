#!/usr/bin python3
# coding: utf-8

# In[148]:


import numpy as np
import matplotlib as plt
import random

ceiling = 2
floor = 0
leftwall = -5.5
rightwall = 5.5
backwall = 14
barriers = 0

p_stickceiling = 0
p_stickfloor = 0
p_stickwall = 0.1
p_stickbackwall = 0
p_stickbarriers = 0
p_sticklamp = 0.2

p_scatterceiling = 0
p_scatterfloor = 0
p_scatterwall = 0.1
p_scatterbackwall = 0
p_scatterbarriers = 0
p_scatterlamp = 0.5

p_reflectceiling = 0
p_reflectfloor = 0
p_reflectwall = 0.1
p_reflectbackwall = 0
p_reflectbarriers = 0
p_reflectlamp = 0.3


#determine a random point on one of the lamps (source)
theta = random.uniform(0,2*np.pi)
radius = 0.1
xlamp = random.randint(-5,5)
zlamp = 0.3*(2*random.randint(0,1)-1)

x_source = xlamp+radius*np.cos(theta)
y_source = random.uniform(floor,ceiling)
z_source = zlamp +radius*np.sin(theta)


#determine a random velocity vector for a photon that doesnt go in the negative x direction
#this means that when theta = 0, the photon will not travel back into the light source
def gen_direction():
    unsolved = True
    while unsolved:

        x_direction1 = random.uniform(0,1)
        y_direction1 = random.uniform(-1,1)
        z_direction1 = random.uniform(-1,1)
        if x_direction1**2+y_direction1**2+z_direction1**2<=1:

            unsolved = False

            return(x_direction1,y_direction1,z_direction1)

x_direction1,y_direction1,z_direction1 = gen_direction()

# rotate our velocity vector by theta
x_flight1 = x_direction1*np.cos(theta)-z_direction1*np.sin(theta)
y_flight1 = y_direction1
z_flight1 = x_direction1*np.sin(theta)+z_direction1*np.cos(theta)

lampbehaviour = random.uniform(0,1)

if lampbehaviour<p_sticklamp:
    print("photon absorbed at")
    print(x_source,y_source,z_source)

else:
    print("photon bounced off from")
    print(x_source,y_source,z_source)
    print("on the ray")
    print(x_flight1,y_flight1,z_flight1)

    ceiling_sct1 = (ceiling-y_source)/y_flight1
    floor_sct1 = (floor-y_source)/y_flight1
    leftwall_sct1 = (leftwall-x_source)/x_flight1
    rightwall_sct1 = (leftwall-x_source)/x_flight1
    backwall_sct = (backwall-z_source)/z_flight1
    barrier_sct = (barriers-z_source)/z_flight1

    a=min(ceiling_sct1,floor_sct1,leftwall_sct1,rightwall_sct1,backwall_sct)
    print(a)
