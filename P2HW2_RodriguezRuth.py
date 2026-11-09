# Ruth Rodriguez
# 11/8/26
# P2HW2
# Write a program that asks the user to enter test grades

# The user needs to enter the numerical grade received for each module. 
# So the inputs will need to be floats to allow for decimal values.

module1 = float(input("Enter grade for module 1: "))
module2 = float(input("Enter grade for module 2: "))
module3 = float(input("Enter grade for module 3: "))
module4 = float(input("Enter grade for module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))

#calculate for the lowest grade 
lowest = min(module1, module2, module3, module4, module5, module6)
highest = max(module1, module2, module3, module4, module5, module6)
total_sum = module1 + module2 + module3 + module4 + module5 + module6
average = total_sum / 6

print()
print("-------------Results-------------")

# display the lowest grade, highest grade, sum of all grades, and average grade using the tips from the previous assignment
# on using < to specify the field width and align characters to the left or the right. 

# Using a width of 18 for the text columns just like before
print(f"{'Lowest Grade:':<18}{lowest:.1f}")
print(f"{'Highest Grade:':<18}{highest:.1f}")
print(f"{'Sum of Grades:':<18}{total_sum:.1f}")
print(f"{'Average Grade:':<18}{average:.1f}")

print("---------------------------------")