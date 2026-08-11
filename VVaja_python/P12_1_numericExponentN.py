# P12_1_numericExponentN.py
# when no analytical solution is possible
# numerical calculation with Newton-Rapshon

import numpy as np
# input data
W0=-608000 #J/kg
Rs=290 #JkgK
T1=293 #K
p2p1=158

# Equation to solve
def R(n,W0,Rs,T1,p2p1):
    return Rs*T1/(n-1)*(1-p2p1**((n-1)/n))-W0

# Define the numerical derivative function of R with respect to q,
# using the central difference method, analytically dRdh=2*q
def derivative_of_R(n,W0,Rs,T1,p2p1,h_step=1e-5):
    return (R(n + h_step,W0,Rs,T1,p2p1) - R(n - h_step,W0,Rs,T1,p2p1)) / (2 * h_step)

napaka_error=0.001  # error margin
q=1.5  # initial guess (this is n, but to keep syntax q is used)

#Newton-Raphson iterative method
RR = 1  # dummy to start while loop
delta = 1  # dummy to start while loop

while (np.abs(RR)>napaka_error) and (np.abs(delta)>napaka_error):
    RR=R(q,W0,Rs,T1,p2p1)  # call function R
    dRdq=derivative_of_R(q,W0,Rs,T1,p2p1)  # call function derivative_of_R
    delta=-RR/dRdq  # newton difference
    q=q+delta  # update q

print ("result n= ", q)  #result n=  1.2691070855792759


