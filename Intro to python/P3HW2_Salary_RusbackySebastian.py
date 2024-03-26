# Sebastian Rusbacky
# 3/24/2024
# P3HW2
# clacs overtime hours, gross pay and payRate via user inputed values
# ps. This actually isn't late just I forgot to add this comment part into my first attempt I didn't realize loll



employeeName = input("Enter employee's name: ")
hoursWorked = int(input("Enter hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

print('--------------------')
print(f"{'Employee name:':<10} {employeeName}")
print()

if hoursWorked < 40:
    regHours = hoursWorked
    overtimeHours = 0
    print(" No Overtime! \n")
else:
    regHours = 40
    overtimeHours = hoursWorked - 40

regHourPay = regHours * payRate
overtimePay = overtimeHours * (1.5 * payRate)
grossPay = regHourPay + overtimePay

print(f"{'Hours Worked':^10}{'Pay Rate':^20}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':^15}{'Gross Pay':^15}")
print('-------------------------------------------------------------------------------------------------------')
print(f"{hoursWorked:^10}{payRate:^20}{overtimeHours:^15}${overtimePay:<15.2f}${regHourPay:<15.2f}${grossPay:<15.2f}")
