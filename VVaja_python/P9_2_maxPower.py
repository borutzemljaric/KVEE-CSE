#P9_2_maxPower.py
# določitev pretoka za maksimalno moč
# calculating optimal flow for max power at given diameter

import numpy as np
import matplotlib.pyplot as plt

# ============================================
# Given data
# ============================================
rho = 1000.0      # density of water [kg/m³]
g = 9.81          # gravity [m/s²]
h_b = 25.0        # gross head [m]
D = 6.0           # diameter [m]
L = 6000.0        # length [m]
n = 0.015         # Manning roughness [s/m^(1/3)]

# ============================================
# Derived geometric parameters
# ============================================
A = np.pi * D**2 / 4.0          # cross-sectional area [m²]
R = D / 4.0                     # hydraulic radius [m]
R_power = R ** (4.0/3.0)        # R^(4/3)

# ============================================
# Constants for head loss formula (Manning)
# Manning head loss: h_f = (n^2 * L * Q^2) / (A^2 * R^(4/3))
# ============================================
k = (n**2 * L) / (A**2 * R_power)   # such that h_f = k * Q^2

# ============================================
# Flow rate range
# ============================================
Q = np.linspace(0, 150, 500)    # flow rate [m³/s]

# ============================================
# Calculations
# ============================================
h_f = k * Q**2                  # head loss [m]
h_net = h_b - h_f               # net head [m]
h_net = np.maximum(h_net, 0)    # net head cannot be negative

P = rho * g * Q * h_net         # power [W]
P_MW = P / 1e6                  # power [MW]

# Optimal flow from derived formula
Q_opt = A * np.sqrt(h_b * R_power / (3 * n**2 * L))
P_opt = rho * g * Q_opt * (h_b - k * Q_opt**2)
P_opt_MW = P_opt / 1e6

# ============================================
# Plotting
# ============================================
plt.figure(figsize=(12, 8))

# Plot 1: Power vs Flow
plt.subplot(2, 2, 1)
plt.plot(Q, P_MW, 'b-', linewidth=2)
plt.plot(Q_opt, P_opt_MW, 'ro', markersize=10, label=f'Optimum: {Q_opt:.1f} m³/s, {P_opt_MW:.1f} MW')
plt.xlabel('Flow Rate Q [m³/s]', fontsize=12)
plt.ylabel('Power P [MW]', fontsize=12)
plt.title('Power vs Flow Rate', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# Plot 2: Head loss and net head vs Flow
plt.subplot(2, 2, 2)
plt.plot(Q, h_f, 'r-', linewidth=2, label='Head Loss $h_f$')
plt.plot(Q, h_net, 'g-', linewidth=2, label='Net Head $h_{net}$')
plt.axhline(y=h_b, color='b', linestyle='--', linewidth=1, label=f'Gross Head $h_b = {h_b}$ m')
plt.xlabel('Flow Rate Q [m³/s]', fontsize=12)
plt.ylabel('Head [m]', fontsize=12)
plt.title('Head Loss and Net Head vs Flow', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Plot 3: Efficiency (net head / gross head) vs Flow
plt.subplot(2, 2, 3)
efficiency = h_net / h_b * 100
plt.plot(Q, efficiency, 'm-', linewidth=2)
plt.xlabel('Flow Rate Q [m³/s]', fontsize=12)
plt.ylabel('Efficiency [%]', fontsize=12)
plt.title('Hydraulic Efficiency ($h_{net}/h_b$) vs Flow', fontsize=14)
plt.grid(True, alpha=0.3)
plt.ylim(0, 105)

# Plot 4: Power vs Net Head (parametric)
plt.subplot(2, 2, 4)
plt.plot(h_net, P_MW, 'c-', linewidth=2)
plt.xlabel('Net Head $h_{net}$ [m]', fontsize=12)
plt.ylabel('Power P [MW]', fontsize=12)
plt.title('Power vs Net Head', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()

# ============================================
# Print results
# ============================================
print("=" * 60)
print("HYDROELECTRIC POWER PLANT ANALYSIS")
print("=" * 60)
print(f"\nGEOMETRIC PARAMETERS:")
print(f"  Diameter D          = {D:.1f} m")
print(f"  Area A              = {A:.3f} m²")
print(f"  Hydraulic radius R  = {R:.3f} m")
print(f"  Length L            = {L:.0f} m")
print(f"  Gross head h_b      = {h_b:.1f} m")
print(f"  Manning n           = {n:.3f} s/m^(1/3)")

print(f"\nOPTIMAL OPERATING POINT:")
print(f"  Optimal flow Q_opt  = {Q_opt:.2f} m³/s")
print(f"  Head loss h_f       = {k * Q_opt**2:.2f} m")
print(f"  Net head h_net      = {h_b - k * Q_opt**2:.2f} m")
print(f"  Max power P_max     = {P_opt_MW:.2f} MW")
print(f"  Velocity V          = {Q_opt / A:.2f} m/s")

print(f"\nHEAD LOSS CONSTANT:")
print(f"  h_f = k * Q², with k = {k:.6f} s²/m⁵")

print("\n" + "=" * 60)

# ============================================
# Additional: Find flow where net head = 0
# ============================================
Q_max_flow = np.sqrt(h_b / k)
print(f"\nMaximum possible flow (h_net = 0): Q_max = {Q_max_flow:.1f} m³/s")