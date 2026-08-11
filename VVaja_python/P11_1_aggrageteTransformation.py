#P11_1_aggrageteTransformation.py
# water heating and vaporising

import numpy as np
import matplotlib.pyplot as plt

# Constants
m_voda = 50  # kg

# Water properties
cp_voda = 4187      # J/kg·K thermal capacity of water
qt_voda = 334*1000       # J/kg  ice melting energy
qi_voda = 2260*1000      # J/kg   evaporating energy
# Ice properties
cp_led = 2108       # J/kg·K
# Steam properties
cp_para = 1996      # J/kg·K

# 🌡 Temperature vector
T = np.array([18, 100, 200])
n = np.arange(len(T) + 1)

# Define energy vector
Q = np.zeros(3)

# 1. Heating water from X°C to 100°C
Q[0] = m_voda * cp_voda * (T[1] - T[0])

# 2. Vaporizing water at 100°C
Q[1] = m_voda * qi_voda

# 3. Heating steam from 100°C to Y°C
Q[2] = m_voda * cp_para * (T[2] - T[1])

print("Q [kJ]:", Q/1000)  #Q [kJ]: [ 17166.7 113000.    9980. ]
print("Total energy [kJ]:", np.sum(Q)/1000) #Total energy [kJ]: 140146.7

# Plot energy steps
plt.figure()
plt.stairs(Q, n, fill=False)
#plt.xlim([0, 5])
plt.ylabel('Energy [kJ]')
plt.xlabel('Phase step')
plt.title(f'Energy required for phase changes \n of m_ledu {m_voda} kg water into overheat steam')
plt.grid(True)
plt.show()

# Heater power
P = 3000  # W

# Time for each step (in hours)
t = Q / P / 3600
print("Time per step [h]:", t)
print("Total time [h]:", np.sum(t))

#Time per step [h]: [ 1.58950926 10.46296296  0.92407407]
#Total time [h]: 12.976546296296295

# For 3 hours- P = 13000  # W