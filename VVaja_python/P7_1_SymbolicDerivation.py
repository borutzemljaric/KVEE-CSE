#P7_1_SymbolicDerivation.py
# simbolično odvajanje, rešitev dP/du=0
# symbolic derivation, find solution for dP/du=0

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ========== SYMBOLIC DERIVATION ==========
# Define symbols
rho, Q, v, u, beta = sp.symbols('rho Q v u beta', real=True, positive=True)

# Power equation: P = ρ * Q * (v - u) * (1 - cosβ) * u
P = rho * Q * (v - u) * (1 - sp.cos(beta)) * u


print("\nPower equation:")
sp.pprint(P)
print("\n")

# Since ρ, Q, and (1-cosβ) are constants, maximize f(u) = (v - u)·u
f = (v - u) * u
print("Function to maximize (ignoring constants):")
sp.pprint(f)
print("\n")

# First derivative
df_du = sp.diff(f, u)
print("First derivative dP/du ∝ d/du [(v-u)·u]:")
sp.pprint(df_du)
print("\n")

# Solve for optimum
optimal_u = sp.solve(df_du, u)[0]
print("Setting derivative to zero and solving for u:")
print(f"  v - 2u = 0  →  u = {optimal_u}")
print("\n")


# ========== NUMERICAL VERIFICATION WITH PLOT ==========
# Given data
g = 9.81          # m/s²
H = 100           # m
d = 0.20          # m (20 cm)
beta_deg = 165    # degrees
beta_rad = np.deg2rad(beta_deg)
rho_val = 1000    # kg/m³

# Calculate parameters
v_val = np.sqrt(2 * g * H)                      # Jet velocity
A = np.pi * (d/2)**2                            # Jet area
Q_val = A * v_val                               # Flow rate

# Power function
P_func = lambda u_val: rho_val * Q_val * (v_val - u_val) * (1 - np.cos(beta_rad)) * u_val

# Generate data
u_range = np.linspace(0, v_val, 200)
power_values = [P_func(u) for u in u_range]

# Find maximum
u_opt = v_val / 2
P_max = P_func(u_opt)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(u_range, np.array(power_values)/1000, 'b-', linewidth=2.5)
plt.axvline(x=u_opt, color='r', linestyle='--', linewidth=2,
            label=f'$u_{{opt}} = v/2 = {u_opt:.1f}$ m/s')
plt.plot(u_opt, P_max/1000, 'ro', markersize=10)

plt.xlabel('Bucket velocity $u$ (m/s)', fontsize=12)
plt.ylabel('Power $P$ (kW)', fontsize=12)
plt.title('Pelton Turbine Power vs. Bucket Velocity\n(Showing maximum at $u = v/2$)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.text(u_opt*0.6, P_max/1000*0.9, f'Maximum power = {P_max/1000:.1f} kW',
         fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

plt.tight_layout()
plt.show()
