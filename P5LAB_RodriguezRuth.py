# Ruth Rodriguez
# November 20, 2026
# P5LAB
# Program will simulate a customer using a self-checkout machine

import random

def disperse_change (change): 

    # Convert the value to an integer by multiplying by 100 and removing the decimal point.
    change = round(change * 100)
    print(f"Change Amount integer: {change}") 

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

    # Determine the if statments to print the number of each coin type.

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


def main(): 
    # Logic goes here 

    # Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You Owe: ${amount_owed:.2f}")

    # Create a variable to represent the amount the customer will put into the machine
    money_inserted = float(input("How much cash will you put in the self-checkout?"))

    #Calculate the change owed to the customer
    change = money_inserted - amount_owed 
    print(f"Change Owed: ${change:.2f}")

    # Call the disperse_change function 
    disperse_change(change)

# Call the main function to start the program 
main()

    