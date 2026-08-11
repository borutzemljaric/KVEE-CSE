# P4_1_praznenje_fsolve.py
# tank discharge/solution using fsolve

import numpy as np
from scipy.optimize import fsolve
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
    # Ensure argument inside log is positive to avoid ValueError
    try:
        term1 = A2 * np.sqrt(2 * g * h0) + Q * np.log(A2 * np.sqrt(2 * g * h0) - Q)
        term2 = A2 * np.sqrt(2 * g * h)  + Q * np.log(A2 * np.sqrt(2 * g * h)  - Q)
        return term1 - term2 - (A2 ** 2 * ti * g / A1)
    except ValueError:
        return 1e6  # return a large value if log argument is invalid

# Solve for each Q and time step
for i, Q in enumerate(Qd):
    h_z = h0
    for j, ti in enumerate(t):
        # Define lambda for current parameters
        func = lambda h: enacba(h, h0, Q, A1, A2, g, ti)
        sol = fsolve(func, h_z)[0]
        h_t[j, i] = sol
        h_z = sol  # Use current height as guess for next step

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