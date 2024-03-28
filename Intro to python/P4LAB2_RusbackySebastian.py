# Sebastian Rusbacky
# 3/28/2024
# P4LAB2
# using range in for loops and while loops

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

while num1 > num2:
    print("Number is too small, Try again!\n")
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
print("You did it right!\n")

for number in range(num1, num2 + 1, 5)
print(number)