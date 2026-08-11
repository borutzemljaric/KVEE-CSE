# P6_2zakrivljenaCev.py
# sile curka na površino/water jet on plane
# koordinatna transformacija/ coordinate transformation

import numpy as np
from numpy.linalg import inv

#reference coordinate system is x,y

#input data
v_1=1 # m/s input velocity
d_1=5 # cm , input diameter
m_dot=1 #kg/s mass flow
alfa=-90*np.pi/180 #input angle convert to radians

#output data
d_2=2.5 # cm , output diameter
beta=-30*np.pi/180 #angle convert to radians

v_2=d_1**2/d_2**2*v_1  # output velocity

def A(delta):  # planar transformation matrix
    return [(np.cos(delta), -np.sin(delta)),(np.sin(delta),np.cos(delta))]

#creating local force vectors, columns
Fa=[m_dot*v_1,0]
Fb=[m_dot*v_2,0]

#calculate K in global coordinate system
K=np.matmul(A(alfa),Fa)-np.matmul(A(beta),Fb)
print('K= ', K) #result K=  [-3.46410162  1.        ]

# angle of K
angle=np.atan(K[1]/K[0])
print('K_angle= ', angle*180/np.pi ) #result K_angle=  -16.10211375198601
