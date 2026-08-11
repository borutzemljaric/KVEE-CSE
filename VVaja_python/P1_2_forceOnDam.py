# P1_2_forceOnDam.py
# calculate force on dam
# note that the force vector origin lays 2/3 below top water level

#libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# input data
rho = 1000  # water density (kg/m^3)
g = 9.81    # gravity (m/s^2)
width = 500 # dam width (m)
H_max = 100 # maximum dam height (m)

# Method 1: Analytical formula
def force_analytical(h):
    """F = (ρgh² × width) / 2"""
    return (rho * g * h**2 * width) / 2

# Method 2: Integration (to show the concept)
def pressure_at_depth(depth):
    """Pressure at given depth: p = ρgh"""
    return rho * g * depth

def force_integral(h):
    """Calculate force using integration F = ∫ p dA"""
    # Force = ∫₀ʰ ρgh × width × dh
    # This demonstrates the concept how to integrate with Python
    result, _ = quad(lambda x: pressure_at_depth(x) * width, 0, h)
    return result

# Calculate for different water heights
heights = np.arange(0, H_max + 5, 5)
forces_analytical = [force_analytical(h) for h in heights]
forces_integral = [force_integral(h) for h in heights]

# Calculate force for full dam
full_force = force_analytical(H_max)
print(f"Force on full dam: {full_force / 1e6:,.2f} MN")
#Force on full dam: 24,525.00 MN


# Create single graph with both methods
plt.figure(figsize=(10, 6))

# Plot both methods
plt.plot(heights, [f/1e6 for f in forces_analytical], 'b-o', linewidth=2, markersize=8,
         label='Analytical: F = (ρgh²·w)/2')
plt.plot(heights, [f/1e6 for f in forces_integral], 'r--x', linewidth=2, markersize=6,
         label='Integral: F = ∫ ρgh·w·dh')

# Mark full dam point
plt.plot(H_max, full_force/1e6, 'ro', markersize=10, label=f'Full dam ({H_max}m)')

# Labels and title
plt.xlabel('Water Height (m)', fontsize=12)
plt.ylabel('Force (MN)', fontsize=12)
#plt.title('Force on Dam vs. Water Height\nAnalytical vs. Integral Method', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()





