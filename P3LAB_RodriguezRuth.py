# Name: Ruth Rodriguez
# Date: 11/15/2026
# Assignment: P3LAB 
# Description: Write a program allows the user to enter a money value with two places after the decimal.

# Get a value from the user.
change = float(input("enter an amount of money: $"))
# print(f"Change Amount: {change}") 

# Convert the value to an integer by multiplying by 100 and removing the decimal point.
change = int(change * 100)

# Calculate the number of dollars
num_dollars = change // 100
change = change - (num_dollars * 100)

# Calculate the number of quarters
num_quarters = change // 25
change = change - (num_quarters * 25)

# Calcuate the number of dimes 
num_dimes = change // 10
change = change - (num_dimes * 10)

# Calculate the number of nickels
num_nickels = change // 5
change = change - (num_nickels * 5)

# At this point the value should be 9 or less, so there is no need to calculate the number of pennies. The value of change is equal to the number of pennies.
num_pennies = change

# Determine the if statements to print the number of each coin type.

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")
