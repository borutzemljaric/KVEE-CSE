# P10_2_finiteDifference.py
# composite wall, finite difference

import numpy as np

# 1. Input data
L=.15 #m   width, finite difference
lamda1=0.7  # W/mK brick thermal conductivity, podatek za opeko
lamda2=0.035  # W/mK polyfoam, podatek za stiropor
lamda3=0.15  # W/mK siporex
Tn= 25 #°C inside temperature
Tz= 0 #°C outside temperature

# 2 Calculate missing boundary temperatures Tu and Td
# Assume that temperatures are far enough to assume double layer wall
#Tu
R=L*(1/lamda1+1/lamda2)
q=(Tn-Tz)/R
Tu=Tz+q*(L/lamda2)
#Td
R=L*(1/lamda1+1/lamda3)
q=(Tn-Tz)/R
Td=Tz+q*(L/lamda3)
#print(Tu, Td) 23.80952380952381 20.58823529411765

# 3. Calculate effective thermal conductivity
lamda23=2*lamda2*lamda3/(lamda2+lamda3)
lamda21=2*lamda2*lamda1/(lamda2+lamda1)
lamda13=2*lamda1*lamda3/(lamda1+lamda3)

# 4. Solving system of 3 linear equations
K=np.array([[ -(lamda23+lamda21+lamda1+lamda13), lamda21, lamda13],
   [lamda21, -(lamda2+2*lamda21+lamda1), 0],
    [lamda13, 0, -(lamda3+2*lamda13+lamda1)]])

f=np.array([-(lamda23*Tz+lamda1*Tn), -(lamda2*Tz+lamda21*Tu+lamda1*Tn), -(lamda3*Tz+lamda1*Tn+lamda13*Td)])

T = np.linalg.solve(K, f) # solve for temperature vector, T=K^(-1)*f
print ('T1,T2,T3= ',T)  #T=  [22.66478141 23.72163572 20.96991992]




