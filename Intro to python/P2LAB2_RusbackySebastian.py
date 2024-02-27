# Sebastian Rusbacky
# 2/27/2024
# P2LAB2
# Learning about math expresstions and f type strings

num1 = float(input("Enter a Float: "))
num2 = float(input("Enter a Second Float: "))
num3 = float(input("Enter a Third Float: "))
num4 = float(input("Enter a Final Float: "))

# get product of vars with *
product = num1 * num2 * num3 * num4

# get average of vars with (+) then /
average = (num1 + num2 + num3 + num4) / 4

# output
print(f"The Product is: {product:.0f}")
print(f"The Average is: {average:.0f}")

print(f"The Product is: {product:.3f}")
print(f"The Average is: {average:.3f}")