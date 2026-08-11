# P4_1_pure_NewtoRaphson.py
# pure Newton-Raphson method
# we have equation q**2=4, goal is to find q

import numpy as np

# Equation to solve
def R(q):
    return q**2-4

# Define the numerical derivative function of R with respect to q,
# using the central difference method, analytically dRdh=2*q
def derivative_of_R(h, h_step=1e-5):
    return (R(h + h_step) - R(h - h_step)) / (2 * h_step)

napaka_error=0.001  # error margin
q=1.8  # initial guess

#Newton-Raphson iterative method (for each ti, and parameter Q calculate h)
RR = 1  # dummy to start while loop
delta = 1  # dummy to start while loop

while (np.abs(RR)>napaka_error) and (np.abs(delta)>napaka_error):
    RR=R(q)  # call function R
    dRdq=derivative_of_R(q)  # call function derivative_of_R
    delta=-RR/dRdq  # newton difference
    q=q+delta  # update q

print ("result q= ", q)  #result q=  2.0000000002355223



