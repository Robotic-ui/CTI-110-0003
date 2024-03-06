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
lowestGrade = min(grades)
highestGrade = max(grades)
gradesSum = sum(grades)

# first slower method to find the average
average = mod1_Grade + mod2_Grade + mod3_Grade + mod4_Grade + mod5_grade + mod6_Grade / 2

# faster way
average = sum(grades) /len(grades)
print(f"Second average method" round(average,3))

print("--------- Results ----------")
print(f"Lowest Grade: {lowestGrade}")
print(f"Highest Grade: {highestGrade}")
print(f"Sum of Grades: {gradesSum}")
print(f"Average: {average}")