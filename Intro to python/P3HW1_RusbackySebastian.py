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
lowest_grade = min(grades)
highest_grade = max(grades)
totalGrade = sum(grades)
average = totalGrade / len (grades)

# determine letter grade for average... I used elif becuase it's just easier to keep track instead of else
print("---------- Results ----------\n")
print(f"Lowest Grade:, {lowest_grade}")
print(f"highest Grade:, {highest_grade}")
print(f"total Grade:, {totalGrade}")
print(f"Average:, {average}")

print("--------------------")

if average >= 90:
    print("Your average grade is: A")
elif average >= 80:
    print("Your average grade is: B")
elif average >= 70:
    print("Your average grade is: C")
else:
    print("Your grade was determined to be below 70 by the programming gods so unfortunately you scored: F")