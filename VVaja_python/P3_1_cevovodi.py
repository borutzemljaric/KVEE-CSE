# P3_1_cevovodi.py

import numpy as np

#pipe network data (element, diameter (cm), length (m))
details=np.array([[1, 2.5, 60],
[2, 2.0, 40 ],[3, 2.0, 50], [4, 1.25, 40]])
nu=0.96e-3 # dynamic viscosity Ns/m2
Qin=0.1 #m3/s

a,b=np.shape(details)  # number of rows, columns
print(a)
print(b)

# calculate resistances
R=np.zeros(a)
for i in range (a):
    R[i]=128*details[i,2]*nu/(np.pi*(details[i,1]*1e-2)**4)
print(R)

RR=np.array([[1/R[0]+1/R[1], -1/R[1], -1/R[0]],
[-1/R[1], (1/R[1]+1/R[2]+1/R[3]) , -(1/R[2]+1/R[3]) ],
[-1/R[0], -(1/R[2]+1/R[3]) , (1/R[0]+1/R[2]+1/R[3])]])

QQ=np.array([Qin,0,-Qin])

#vector of pressures
P=np.linalg.solve(RR, QQ) #solution of a x = b for x
print('Pi= ',P)  # chose reference pressure
P=P-P[2]
print('Pi= ',P)  # N/m2

#vector of flows
Qi=np.array([(P[0]-P[2])/R[0],(P[0]-P[1])/R[1],(P[1]-P[2])/R[2],(P[1]-P[2])/R[3]])
print('Qi= ',Qi)  #m3/s