fav_flavour = input("Which flavor do you want?").strip().lower()


# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

# Case 1:
# Yes, we do have vanilla
# Case 2:
# "orange"
# Sorry, we ran out of orange
# if fav_flavour == stock1:
#     print("Yes, we do have vanilla")
# elif fav_flavour == stock2:
#     print(f"Yes, we do have {fav_flavour}")
# elif fav_flavour == stock3:
#     print(f"Yes, we do have {fav_flavour}")
# elif fav_flavour == stock4:
#     print(f"Yes, we do have {fav_flavour}")
# else:
#     print(f"Sorry, we ran out of {fav_flavour}")

# Task 1.2
# Clue: Logical Operators 2(or)
# if (fav_flavour == stock1) or (fav_flavour == stock2) or (fav_flavour == stock3):

# Array/ List
if fav_flavour in [stock1, stock2, stock3, stock4]:
    print(f"Yes, we do have {fav_flavour}")
else:
    print(f"Sorry, we ran out of {fav_flavour}")

# ctr + ,
