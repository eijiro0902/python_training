# Case 1:
# Luffy, Zoro
# 173cm, 163cm
# Expected
# Luffy is taller than Zoro by 10cm

captain_name = input("Captain name?")
captain_height = int(input("Captain height?"))
solders_name = input("Solders name?")
solders_height = int(input("Solders height?"))

if captain_height >= solders_height:
    diff = captain_height - solders_height
    print(f"{captain_name} is taller than {solders_name} by {diff}")
else:
    diff = solders_height - captain_height
    print(f"{solders_name} is taller than {captain_name} by {diff}")

# Case 2:
# Luffy, Zoro
# 173cm, 185cm
# Expected
# Zoro is taller than Luffy by 12cm
