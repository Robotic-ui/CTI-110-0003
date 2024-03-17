# Sebastian Rusbacky
# 3/17/2024
# P3LAB - Branching
# Exact change lab | Gets change owed from user

change = int(input("Enter an amount of change as an integer: "))

if change == 0:
    print("You owe no $ amount | input change = 0")

# calc the amount of each coin needed
numDollars = change // 100
change = change - (numDollars * 100)

numQuarters = change // 25
change = change - (numQuarters * 25)

numDimes = change // 10
change = change - (numDimes * 10)

numNickles = change // 5
change = change - (numNickles * 5)

numPennies = change // 1

# output
if numDollars > 0:
    print(numDollars, end = " ")
    if numDollars == 1:
        print("Dollar")
    else:
        print("Dollars")

if numQuarters > 0:
    print(numQuarters, end = " ")
    if numQuarters == 1:
        print("Quarter")
    else:
        print("Quarters")

if numDimes > 0:
    print(numDimes, end = " ")
    if numDimes == 1:
        print("Dime")
    else:
        print("Dimes")

if numNickles > 0:
    print(numNickles, end = " ")
    if numNickles == 1:
        print("Nickle")
    else:
        print("Nickles")

if numPennies > 0:
    print(numPennies, end = " ")
    if numPennies == 1:
        print("Penny")
    else:
        print("Pennies")