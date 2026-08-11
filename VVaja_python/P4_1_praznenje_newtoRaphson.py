# P4_1_praznenje_newtoRaphson.py
# tank discharge/solution using Newton-Raphson method

import numpy as np
import matplotlib.pyplot as plt

# Input data
A1 = 300 # Tank area (m)
A2 = 0.8 # Orifice area (m)
h0 = 20 # Tank height (m)
g = 9.81 #gravity (m/s2)

# Inflow rates (m3/s)
Qd = [0, 5, 10, 15]
n_Q = len(Qd)

# Time array (s)
t = np.arange(1, 701)  # 701 is taken, could be different
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
h_z=h0  # initial condition

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

# Plotting
plt.plot(t, h_t[:, 0], label='Q = 0 m$^3$/s')
plt.plot(t, h_t[:, 1], label='Q = 5 m$^3$/s')
plt.plot(t, h_t[:, 2], label='Q = 10 m$^3$/s')
plt.plot(t, h_t[:, 3], label='Q = 15 m$^3$/s')

plt.xlabel('t [s]')
plt.ylabel('h [m]')
#plt.title('')
plt.legend()
plt.grid(True)
plt.show()