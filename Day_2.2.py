# # Task 2.2: With f-string | Clue: round()
# # Fahrenheit to celsius
# # Please provide your Fahrenheit: 100
# # The 100°F is 37.78°C

temp_f = float(input("temperture?"))
temp_c = (temp_f - 32) * (5/9)

int_temp_f = int(temp_f)
rounded_temp_c = round(temp_c, 2)
print(f'The {int_temp_f}F is {rounded_temp_c}C')