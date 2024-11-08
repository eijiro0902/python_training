# Loops
# Repeating statement

# i = 2
# while i <= 3:
#     print("Hello")
#     i = i+1

# Task - 1
# Expected output
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥

# fire_rows = int(input("How many rows?"))

# i = 1
# n = 1
# # while i <= (fire_rows):
# #     print(" " * (fire_rows - (i)) + "🔥" * (i))
# #     i = i + 2

# while n <= (fire_rows):
#     print(" " * (fire_rows - (i)) + "🔥" * (i))
#     i = i + 2
#     n = n + 1

# Loop(for)
# range(3)   0,1,2
# range(1,4) 1,2,3,
# r = 3

# r = int(input("Fire rows?"))

# for i in range(r):
#     print("🔥" * (i + 1))

# for in in range(1,5):
#     print("🔥"* i)


####################################################

# Task 1.2 - Convert below to for loop

# i = 1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# while i <= rows:
#     print(pattern * i)
#     i = i + 1

rows = int(input("Please tell the no of rows?: "))
pattern = input("Please tell the pattern?: ")

for i in range(1, rows + 1):
    print(pattern * i)
