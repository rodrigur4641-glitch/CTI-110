# Ruth Rodriguez
# October 30, 2026
# P1HW2
# Create a travell budget 

print("This program calculates and dispays travel expenses")
print()

budget = input("Enter budget: ")
print()
destination = input("Enter your travel destination: ")
print()
gas = input("How much do you think you will spend on gas? ")
print()
hotel = input("Approximately, how much will you need for accomodation/hotel? ")
print()
food = input("Last, how much do you need for food? ")
print()

print("------------Travel Expenses------------")
print("Location: " + destination)
print("Initial Budget: " + budget)
print()
print("Fuel: " + gas)
print("Accomodation: " + hotel)
print("Food: " + food)
print()
print("Remaining Balance: " + str(int(budget) - (int(gas) + int(hotel) + int(food))))

# For the ramiainig balance line I had to look up some more videos to try and understand why this line of code was not working like the previous HW assignment. 
# I had to use the str() function so that the final numbber would display as a string and not an integer. 


