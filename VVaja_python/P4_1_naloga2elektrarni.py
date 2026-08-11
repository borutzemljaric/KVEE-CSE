# P4_1_naloga2elektrarni.py
# tank discharge/solution using Newton-Raphson method

import numpy as np
import matplotlib.pyplot as plt

# Input data
V=6000 #m3 Tank volume

A2 = 0.8 # Orifice area (m)
h0 = 20 # Tank height (m)
g = 9.81 #gravity (m/s2)
A1 = V/h0 # Tank area (m)

# normal operation 5 min, inflow 12 m3/s,
# the code from P4_1_praznenje_newtoRaphson.py is appropriate,
# change vector t, Q into vector with one dimension

# Inflow rates (m3/s)
Qd = [12]
n_Q = len(Qd)

# Time array (s)
t = [300] # instead of np.arange(1, 701)  # 701 is taken, could be different
n_t = len(t)

# Initialize result matrix rows-flow, column-parameter
h_t = np.zeros((n_t, n_Q))


# Equation to solve
def enacba(h, h0, Q, A1, A2, g, ti):
    term1 = A2 * np.sqrt(2 * g * h0) + Q * np.log(A2 * np.sqrt(2 * g * h0) - Q)
    term2 = A2 * np.sqrt(2 * g * h)  + Q * np.log(A2 * np.sqrt(2 * g * h)  - Q)
    return term1 - term2 - (A2 ** 2 * ti * g / A1)

# Define the numerical derivative function with respect to h,
# using the central difference method
def derivative_enacba(h, h0, Q, A1, A2, g, ti, h_step=1e-5):
    return (enacba(h + h_step, h0, Q, A1, A2, g, ti) - enacba(h - h_step, h0, Q, A1, A2, g, ti)) / (2 * h_step)


napaka_error=0.001  # error margin
h = h0 # initial condition

# Solve for each Q and time step
for i, Q in enumerate(Qd):
    h = h0 # initial condition
    for j, ti in enumerate(t):

        #Newton-Raphson iterative method (for each ti, and parameter Q calculate h)
        RR = 1  # dummy to start while loop
        delta = 1  # dummy to start while loop
        while (np.abs(RR)>napaka_error) and (np.abs(delta)>napaka_error):
            RR=enacba(h, h0, Q, A1, A2, g, ti)
            DR=derivative_enacba(h, h0, Q, A1, A2, g, ti)
            delta=-RR/DR
            h=h+delta

        h_t[j, i]=h  # write result into matrix

print(f'height after {t} s in [m]', h_t)


#delete Graph


# the rest needed time, to drop water from h_t to h0/2

t_2=-A1/(g*A2)*(np.sqrt(2*g*h0/2)-np.sqrt(2*g*h_t[0]))

print(f'free discharge time [s]', t_2)
print(f'total time [s]', t[0]+t_2)

#height after [300] s [[16.8409849]]
#free discharge time [s] [159.41593784]
#total time [s] [459.41593784]
