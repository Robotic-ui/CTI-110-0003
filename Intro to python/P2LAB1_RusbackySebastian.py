# Sebastian Rusbacky
# 2/27/2024
# P2LAB1
# Learning about math expresstions and f type strings 

mpg = float(input("Enter the Cars Miles Per Gallon: "))
cost_fuel = float(input("How much does One Gallon cost: "))

# clac $ of driving 20 miles
miles20 = (20 / mpg) * cost_fuel

# calc $ of driving 75 miles
miles75 = (75 / mpg) * cost_fuel

# calc $ of driving 500 miles
miles500 = (500 / mpg) * cost_fuel

# output
print(f"Cost to drive 20 Miles is ${miles20:.2f}")
print(f"Cost to drive 75 Miles is ${miles75:.2f}")
print(f"Cost to drive 500 Miles is ${miles500:.2f}")