# Sebastian Rusbacky
# 2/29/2024
# P2HW2
# Accessing a user entered list then dsplaying lowestGrade, highestGrade, the sum of all the grades and average 

mod1_Grade = float(input("What is your Grade for Module 1? "))
mod2_Grade = float(input("What is your Grade for Module 2? "))
mod3_Grade = float(input("What is your Grade for Module 3? "))
mod4_Grade = float(input("What is your Grade for Module 4? "))
mod5_grade = float(input("What is your Grade for Module 5? "))
mod6_Grade = float(input("What is your Grade for Module 6? "))

grades = [mod1_Grade, mod2_Grade, mod3_Grade, mod4_Grade, mod5_grade, mod6_Grade]

print("--------- Results ----------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {grades_sum}")
print(f"Average: {average}")