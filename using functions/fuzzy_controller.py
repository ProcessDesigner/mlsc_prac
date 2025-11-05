import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature') # 0–40°C
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')
# 0–100%
# Define fuzzy membership functions for Temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 15])
temperature['warm'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])
# Define fuzzy membership functions for Fan Speed
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])
# Define fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])
# Build control system
fan_ctrl_system = ctrl.ControlSystem([rule1, rule2, rule3])
fan = ctrl.ControlSystemSimulation(fan_ctrl_system)
# Test: Set input temperature value
input_temp = 28
fan.input['temperature'] = input_temp
# Compute result
fan.compute()
# Display output
print(f"\n===== FUZZY CONTROLLER SYSTEM =====")
print(f"Input Temperature : {input_temp}°C")
print(f"Output Fan Speed : {fan.output['fan_speed']:.2f}%")
print("===================================\n")
# Visualize results
temperature.view()
plt.figure()
fan_speed.view(sim=fan)
plt.show()