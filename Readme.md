Capacitor Charging and Discharging Simulation Tool

What is Capacitor and their application?
Capacitors are devices that store electric charge and energy, playing a vital role in various applications.They are commonly used as filters in DC power supplies and as energy storage banks for pulsed lasers.
One of their key characteristics is the ability to pass AC current while blocking DC current, which makes them essential in applications where the AC component of a signal needs to be measured.
Capacitors are also widely used in plasma physics, where their energy-storing capability is utilized for various experiments and applications.A capacitor can be slowly charged to the necessary voltage and then discharged
quickly to provide the energy needed. It is even possible to charge several capacitors to a certain voltage and then discharge them in such a way as to get more voltage.

This assignment features an RC circuit, which is one of the simplest circuits that uses a capacitor.

Introduction

This simulation tool demonstrates the charging and discharging behavior of a capacitor connected in series with a resistor (RC circuit). Users can input the resistance, capacitance, and input voltage values to observe the corresponding voltage changes over time.

The parameter we used for the simulation are listed below:

Resistance (R): Enter the resistance value in ohms.
Capacitance (C): Enter the capacitance value in farads.
Input Voltage (Vin): Enter the input voltage value in volts.

Start Simulation: Run the code to begin the simulation.

Visualization: The tool will display two graphs:

Charging Curve: Shows the increase in capacitor voltage over time as it charges.
Discharging Curve: Shows the decrease in capacitor voltage over time as it discharges.
Adjust Parameters: Modify the input parameters and run the code again to observe the effects on the charging and discharging curves.

Interpretation:

Charging Curve: The capacitor voltage initially increases rapidly, then gradually approaches the input voltage. The rate of increase depends on the RC time constant (R * C).
Discharging Curve: The capacitor voltage decreases exponentially over time, eventually reaching zero. The rate of decrease also depends on the RC time constant.
Charging a Capacitor
When a capacitor is charged through a resistor 𝑅R with a voltage source 𝑉0, the voltage across the capacitor 𝑉(𝑡)
V(t) as a function of time 𝑡 is given by:
𝑉(t)=𝑉0(1−𝑒^−𝑡/𝑅𝐶)
where:
R is the resistance in ohms,
C is the capacitance in farads,
e is the base of the natural logarithm,
t is the time in seconds.
The time constant 𝜏
τ of the circuit is defined as:
τ=RC
This time constant represents the time it takes for the voltage to reach about 63.2% of its maximum value v0.

Discharging a Capacitor
For discharging, when the capacitor discharges through a resistor 𝑅 (with no external voltage source), the voltage across the capacitor decreases over time according to:
𝑉(𝑡)=𝑉0𝑒^−𝑡/𝑅C
where 
𝑉0 is the initial voltage across the capacitor at 𝑡=0.
Key Points
Charging Equation: 
𝑉(𝑡)=𝑉0(1−𝑒^−𝑡/𝑅𝐶)
Discharging Equation: 
𝑉(𝑡)=𝑉0(𝑒^−𝑡/𝑅𝐶) 
Time Constant: 
𝜏=𝑅𝐶 determines how quickly the capacitor charges and discharges.
