# P6_1koordinatneTransformacije.py
# sile curka na površino/water jet on plane
# koordinatna transformacija/ coordinate transformation

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

#reference coordinate system is x,y

#input data, water jet A
D=0.1 #m diameter of jets (same to jet B)
Q=0.03 #m3/s volume flow
rho=1000 # kg/m3
alpha=-60*np.pi/180 #angle convert to radians

# water jet B
m_dot=30 #kg/s mass flow
beta=30*np.pi/180 #angle convert to radians

# plane
delta=45*np.pi/180 #angle convert to radians

def A(delta):  # planar transformation matrix
    return [(np.cos(delta), -np.sin(delta)),(np.sin(delta),np.cos(delta))]

# jets absolute forces
Fa_abs=rho*Q**2*4/(np.pi*D**2)
Fb_abs=m_dot**2*4/(rho*np.pi*D**2)
#print ('Fabs= ', Fa_abs, Fb_abs)  #see for convenience

#creating local force vectors, columns
Fa=[Fa_abs,0]
Fb=[Fb_abs,0]

#calculate both forces in global coordinate system
Fs=np.matmul(A(alpha),Fa)+np.matmul(A(beta),Fb)
print('Fs= ', Fs) #see for convenience

#convert forces in plate local coordinate system
A_inverse=inv(A(delta)) #inverse shown for better readability
Fp_local=np.matmul(A_inverse,Fs)
print('Fp_local= ', Fp_local) #see for convenience

#At this point we should take into account that only normal force of jet stream
# act , the tangential is neglected, in our case should be 'manually' set to zero
Fp_local[0]=0  # Fp_local is vector, in local coordinate first coordinate is tangential

# to calculate forces in global coordinate system
Fp_global=np.matmul(A(delta), Fp_local)
print('Fp_global= ', Fp_global) #result Fp_global=  [ 99.13093836 -99.13093836]

#Fabs=  114.59155902616465 114.59155902616463
#Fs=  [156.53498069 -41.94342166]
#Fp_local=  [  81.02846845 -140.34542422]
#Fp_global=  [ 99.23920118 -99.23920118]