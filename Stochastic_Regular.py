# -*- coding: utf-8 -*-
"""Stochastic_Regular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/raz-mon/Thermo2_Project/blob/main/Stochastic_Regular.ipynb
"""

pip install pythran

import numpy as np
import math
import pandas as pd
import pythran
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %load_ext pythran.magic

#np.random.seed(123)
mu = 0.002
def sir(u,parms,t):
    
    bet,gamm,iota,N,dt=parms
    S,I,R,Y=u
    lambd = bet*(I+iota)/N
    ifrac = 1.0 - math.exp(-lambd*dt)
    rfrac = 1.0 - math.exp(-gamm*dt)
    dfrac = 1.0 - math.exp(-mu*dt)
    infection = np.random.binomial(S,ifrac)
    recovery = np.random.binomial(I,rfrac)
    #death_S = np.random.binomial(S, dfrac)
    #death_I = np.random.binomial(I, dfrac)
    #death_R = np.random.binomial(R, dfrac)
    return [S-infection,I+infection-recovery,R+recovery,Y+infection]

# Here we change the value of beta from 0.1 to 0.1+0.01 * 50 = 0.51, mu = 0.00002
def simulate():
    parms = [0.2, 0.1, 0.01, 1000.0, 0.1]
    tf = 2000
    tl = 2000
    t = np.linspace(0,tf,tl)
    S = np.zeros(tl)
    I = np.zeros(tl)
    R = np.zeros(tl)
    Y = np.zeros(tl)
    u = [999,1,0,0]
    S[0],I[0],R[0],Y[0] = u
    for j in range(1,tl):
        u = sir(u,parms,t[j])
        S[j],I[j],R[j],Y[j] = u
    return {'t':t,'S':S,'I':I,'R':R,'Y':Y}

sir_out = pd.DataFrame(simulate())



sline = plt.plot("t","S","",data=sir_out,color="blue",linewidth=2)
iline = plt.plot("t","I","",data=sir_out,color="red",linewidth=2)
rline = plt.plot("t","R","",data=sir_out,color="green",linewidth=2)


#plt.ylim([0,700])
#plt.xlim([0,50])
plt.title("beta: " + str(0.2) + ", gamma: " + str(0.05) + ", mu: " + str(round(mu, 5)))
plt.xlabel("Time",fontweight="bold")
plt.ylabel("N",fontweight="bold")


legend = plt.legend(loc=5,bbox_to_anchor=(1.25,0.5))
frame = legend.get_frame()
frame.set_facecolor("white")
frame.set_linewidth(1)

plt.grid(color='w', linewidth=3)
ax = plt.axes()
ax.set_facecolor('whitesmoke')

