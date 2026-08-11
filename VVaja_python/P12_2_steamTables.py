# P12_2_steamTables.py
# specific volume, enthalpy, entropy

import numpy as np
# input data
m=1 #kg
x=0.9 # steam content

#from table 2
v1=1.138 #cm3/g ( *1e-3 to get m3/kg!)
v2=163.2 #cm3/g
h1=798.33 #J/kg
h2=2783.7 #J/kg
s1=2.21 #J/kgK
s2=6.52 #J/kgK

v=(1-x)*v1+x*v2  # specific values (on kg)
h=(1-x)*h1+x*h2
s=(1-x)*s1+x*s2


print ("v ", v," h ", h," s ", s )  #result v  146.99  h  2585.16  s  6.088



