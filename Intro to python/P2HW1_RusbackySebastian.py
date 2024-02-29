# Sebastian Rusbacky
# 2/20/2024
# P2HW1
# Does some basic math with user entered vars

userBudget = int(input("What is your Budget? "))
travelDest = str(input("What is your travel Destination? "))
userFuel = int(input("How will you need for petrol?  "))
userAccommodation = int(input("Aprox how much will you need for accommodations? "))
userFood = int(input("Finally, How much money will you need for food? "))

print("\n ---------- Travel Expenses ----------")
print("Location:", travelDest)
print(f"Inital Budget: ${userBudget:.2f}")

print(f"Fuel: ${userFuel:.2f}")
print(f"Accommodation: ${userAccommodation:.2f}")
print(f"Food: ${userFood:.2f}")
print("----------------------------------------")

print("Remaining Balance:", userFuel - userAccommodation - userFood)