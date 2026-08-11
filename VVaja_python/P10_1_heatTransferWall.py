# P10_1_heatTransferWall.py
# composite wall, temperature at layer boundaries and heat transfer

import numpy as np

# 1. Input data
L1=.25 #m  brick width, debelina opeke
L2=.15  #m  polyfoam width, debelina izolacije
lamda1=0.7  # W/mK brick thermal conductivity, podatek za opeko
lamda2=0.035  # W/mK polyfoam, podatek za stiropor
alfa=5  # W/m2K  #heat transfer coefficient, na obeh straneh enak
A=6*3  # wall area,  površina zidu

Tn= 25 # inside temperatrure, stopinj celzija
Tz= -5 # outside temperature, stopinj celzija

# 2. Solving
# energy balance approach / in node the teat transfer is the same (Q_1=Q_2)
# izračun z energijsko bilanco

K=np.array([[ lamda1*A/L1+alfa*A, -lamda1*A/L1, 0],
   [-lamda1*A/L1, lamda1*A/L1+lamda2*A/L2, -lamda2*A/L2],
    [0, -lamda2*A/L2, lamda2*A/L2+alfa*A]])

f=np.array([alfa*A*Tn, 0, alfa*A*Tz])  # vector of external heat

T = np.linalg.solve(K, f) # solve for temperature vector, T=K^(-1)*f
print ('T= ',T)

# calculate wall heat transfer, izračun izgub,
pfi=alfa*A*(Tn-T[0])  # W
print ('pfi= ',pfi)

#T =23.8102, 21.6856,-3.8102
#pfi=  107.08

