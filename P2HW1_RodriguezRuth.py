 # Ruth Rodriguez
 # 11/8/26
 # P2HW1
 # Reorganizing P1HW2 so that the results are printed in a more organized manner.

print("This program calculates and dispays travel expenses")
print()

budget = float(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))

remaining_balance = budget - gas - hotel - food
print()

print("------------Travel Expenses------------")
print(f"{'Location:':<18}{destination}")
print(f"{'Initial Budget:':<18}${budget:.2f}")
print(f"{'Fuel:':<18}${gas:.2f}")
print(f"{'Accommodation:':<18}${hotel:.2f}")
print(f"{'Food:':<18}${food:.2f}")
print("--------------------------------------")
print()
print(f"Remaining Balance: ${remaining_balance:.2f}")



