# Sebastian Rusbacky
# 3/17/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# finds min, max, sum and average for the list
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len (grades)

# determine letter grade for average... I used elif becuase it's just easier to keep track instead of else
if avg >= 90:
    print("Your average grade is: A")
elif avg >= 80:
    print("Your average grade is: B")
elif avg >= 70:
    print("Your average grade is: C")
else:
    print("Your grade was determined to be below 70 by the programming gods so unfortunately you scored: F")