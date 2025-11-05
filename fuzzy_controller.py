import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')   # 0–40°C
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')      # 0–100%

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
print(f"Output Fan Speed  : {fan.output['fan_speed']:.2f}%")
print("===================================\n")

# Visualize results
temperature.view()
plt.figure()
fan_speed.view(sim=fan)
plt.show()


# DOne by gurdev


# import numpy as np
# def fuzzify_error(e):
#     low = max(0, min(1, 1 - e))
#     medium = max(0, min(1, 1 - abs(e - 0.5)/0.5))
#     high = max(0, min(1, e))
#     return np.array([low, medium, high])
# def fuzzify_change(ec):
#     neg = max(0, min(1, -ec))
#     zero = max(0, min(1, 1 - abs(ec)))
#     pos = max(0, min(1, ec))
#     return np.array([neg, zero, pos])
# def defuzzify(output):
#     weights = np.array([-1, 0, 1])
#     return np.dot(output, weights) / np.sum(output)
# rules = np.array([
# [0, -1, -1],
# [0, 0, 0],
# [0, 1, 1],
# [1, -1, -1],
# [1, 0, 0],
# [1, 1, 1],
# [2, -1, -1],
# [2, 0, 0],
# [2, 1, 1]
# ])
# error = 0.6
# change = 0.2
# e_membership = fuzzify_error(error)
# ec_membership = fuzzify_change(change)
# output_membership = np.zeros(3)
# for rule in rules:
#     e_idx, ec_idx, out_idx = rule
#     firing_strength = min(e_membership[e_idx], ec_membership[ec_idx])
#     output_membership[out_idx] = max(output_membership[out_idx], firing_strength)
# control_signal = defuzzify(output_membership)
# print("Error Membership:", e_membership)
# print("Change Membership:", ec_membership)
# print("Output Membership:", output_membership)
# print("Control Signal:", control_signal)