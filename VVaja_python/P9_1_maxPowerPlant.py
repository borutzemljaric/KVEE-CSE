# P9_1_maxPowerPlant.py
# optimization problem of hydroelectric power plant

import numpy as np
from scipy.optimize import Bounds, LinearConstraint,minimize

# Input data
Q=np.array([50,100,166, 250, 400]) # Flow cases  (m3/s)
n_Q = len(Q) # number of elements
ro = 1000 # density of water (kg/m3)
g = 9.81 #gravity (m/s2)
h= 11 # head (m)
h_water=0.9 # change of downstream water (m)
Q_max=500 # maximum water flow (m3/s)

Qn=166.67 # nominal flow for one turbine (m3/s)
Pn=16.23  # nominal power for one turbine (MW)


#------------------------------------------------------------------------------
# creating interpolation function for efficiency data from table data
eta_table=np.array([[0,0],
[6,10],
[10,30],
[15,	52],
[20,	61],
[25,	70],
[30,	75],
[35,	79],
[40,	82],
[45,	85],
[50,	87],
[55,	89],
[60,	90],
[65,	90],
[70,	90.5],
[75,	91],
[80,	91.5],
[85,	91.5],
[90,	90.5],
[95,	90.5],
[100,	90]])

z = np.polyfit(eta_table[:,0], eta_table[:,1], 4)  #Least squares polynomial fit.

def efficiency(z,x):
    y = z[0]*x**4 + z[1]*x**3 + z[2]*x**2 + z[3]*x + z[4] # x should be percent
    return y/100  # y is in percents, so result is divided by 100

#------------------------------------------------------------------------------
# create head (height) vector from flow
def h_loss(Q,Q_max,h_water):
    h_l=h_water*Q/Q_max
    return h_l

h_ll=h_loss(Q,Q_max,h_water)
h=h-h_ll
#print (h) # to verify head (m)

#------------------------------------------------------------------------------
# Define the problem and solution
def enacbaSumPowers(Qi, ro,g,hh,z):
    # Ensure argument inside log is positive to avoid ValueError
    term1 = efficiency(z,Qi[0]/Qn*100)*ro*g*hh*Qi[0]  #turbine power  1
    term2 = efficiency(z,Qi[1]/Qn*100)*ro*g*hh*Qi[1]  #turbine power  2
    term3 = efficiency(z,Qi[2]/Qn*100)*ro*g*hh*Qi[2] #turbine power  3
    return -(term1 + term2 + term3) #To find a maximum using scipy, you use a trick, minimize the negative of your objective function

i=0  # flow case,the flow is selected manually (iterations are avoided for clarity of the procedure),
Q_0 = np.array([Q[i]/3, Q[i]/3, Q[i]/3])  #Initial guess for flow

# Define the bounds for turbine power 0<= Qi<=Qn
Q_bounds = Bounds([0, 0, 0], [Qn,Qn,Qn])
# Define the constraint for whole flow Q1+Q2+Q3=Q
Q_linear_constraint = LinearConstraint([[1, 1, 1]], [Q[i]], [Q[i]])
# find maximum in scipy function minimize
res = minimize(enacbaSumPowers, Q_0,args=(ro,g,h[i],z), method='trust-constr', bounds=Q_bounds, constraints=[Q_linear_constraint],options={'verbose': 1})

# Results
print("Optimal flow distribution (m3/s):", res.x)
print("Maximum power output (MW):", -res.fun / 1e6)


