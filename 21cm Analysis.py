#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import pylab as pl



def v_rotationplot(txt_file):
    
    # take in the values and arrange in arrays
    file = open(txt_file,'r')
    everything = []
    
    for line in file:
        everything += line.splitlines()
    
    # we want to start parsing from the second line
    start_index = 1
    
    # l, vleft and vlsr values in arrays
    l = []
    v_left = []
    vlsr = []
    
    for j in range(start_index,len(everything)):
        temp = everything[j].split()
        l.append(temp[0].replace(',',''))
        v_left.append(temp[1].replace(',',''))
        vlsr.append(temp[2])
     
    
    # values of R0= 8.0 +/- 0.4 kpc and Ω0 = 27.2 km/s/kpc -- cf
    l = np.array(np.float_(l))
    v_left = np.array(np.float_(v_left))
    vlsr = np.array(np.float_(vlsr))


    R0 = 8
    Omega_0 = 27.2 
    # then calculate r units in kpc
    r = R0*np.sin(l*np.pi/180)
    print(r)
    
    # Calculate v_prime
    v_prime = vlsr - v_left


    # combine the two to get v(r)
    v = v_prime + r*Omega_0
    
    # creating the fit function
    z = np.polyfit(r,v,3)
    f = np.poly1d(z)
    
    r_new = np.linspace(r[0],r[-1],50)
    v_new = f(r_new)
    
    
    # plot v vs r
    
    fig, axis = plt.subplots(2)
    
    fig.suptitle('Velocity Rotation Curve')
    axis[0].plot(r,v,)
    axis[1].plot(r,v,'o',r_new,v_new)
    plt.xlabel("Radius from center of the galaxy (kpc)")
    plt.ylabel("Circular velocity (km/s)")
    #plt.title('Velocity Rotation Curve')
    plt.xlim([r[0]-1, r[-1] + 1 ])
    
    


v_rotationplot('Velocities.txt')

