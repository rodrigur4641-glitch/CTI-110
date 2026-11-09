 # Ruth Rodriguez
 # 11/7/26
 # P2LAB2
 # Using Dictionaries to store and retrieve data

cars = {'Camero':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#Get keys from the dictionary 
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

#Get a car from user which is just going to be a string
car_name = input("Enter a car: ")

#Get miles per galon for any given car that the user types in
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get how many miles the user wants to drive the car that they typed in
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate how many gallons of gas will be used for a given car for a given amount of miles driven
gallons_needed = miles_driven / car_mpg 

#Display how many gallons of gas will be used for a given car for a given amount of miles driven
print(f"{gallons_needed:.2f} gallon(s) of gas will be used to drive the {car_name} for {miles_driven} miles.")