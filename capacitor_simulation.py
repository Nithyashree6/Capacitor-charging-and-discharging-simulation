import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Constants
R = 1.0  # Resistance (Ohms)
C = 1.0  # capacitor in Farad(F)
V0 = 5.0  # Initial voltage (volts)
tau = R * C  # Time constant

# Time values
t = np.linspace(0, 5 * tau, 500)

# Charge functions for charging and discharging
Capacitor_charging = V0 * (1 - np.exp(-t / tau))
Capacitor_discharging = V0 * np.exp(-t / tau)

# Create plots
plt.figure(figsize=(12, 6))

# Plot charging
plt.subplot(121)
plt.plot(t, Capacitor_charging, label='Charging Voltage (V)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Charging in RC circuit')
plt.grid()
plt.legend()

# Plot discharging
plt.subplot(122)
plt.plot(t, Capacitor_discharging, label='Discharging Voltage (V)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Discharging in RC circuit')
plt.grid()
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
