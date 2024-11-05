# Task 2.1: With f-string
# Fahrenheit to Celcius
# Please provide your Fahrenheit: 98.6
# The 98.6°F is 37°C
# °C = (°F - 32) × 5/9

temp = float(input('temperture in F?'))
t_c = (temp - 32) * (5/9)
print(f'C:{temp},F:{t_c}')

