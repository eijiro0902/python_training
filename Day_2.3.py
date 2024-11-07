#[start:end:skip]

# print(name.upper())
# var.lower()
# var.strip() #remove space

# Task 1.1
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Clue:
# Slice operator

# Expected Output
# "PYTHON-POWERFUL"

# upper = secret_message.upper()
# print(upper[18:24]+'-'+upper[25:30])


#####################################
# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

lower = flipped_message.lower()
lower = lower[::-1]
print(lower[0:6]+" 🗡️  "+lower[12:20]+" 🌸 ")


