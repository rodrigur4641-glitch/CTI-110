# Ruth Rodriguez
# 11/15/26
# P3HW2
# Salary Calculator

# Request employees information
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate overtime 
if hours > 40:
    # calculate the overtime hours 
    overtime_hours = hours - 40 
    # calculate the over pay 
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    # calculate the regular pay 
    regular_pay = 40 * pay_rate 
    # calcuate the gross pay 
    gross_pay = regular_pay + overtime_pay 
else:
    overtime_pay = 0
    overtime_hours = 0 
    regular_pay = hours * pay_rate
    gross_pay = regular_pay


# Display the results 
print("-----------------------------------------------------------------------------------------------")
print("Employee Name: ", name)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
print("-----------------------------------------------------------------------------------------------")
print(f'{hours:<15}{pay_rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')