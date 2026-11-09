 #Ruth Rodriguez  
 #11/06/2026
 #P2LAB1
 #The program will calculate the diameter, circumference, and area of a circle.

#Import the math module to use the value of pi
import math

#get the radius from the user
radius = float(input("What is the radius of the circle? "))
print()

#calculate the diameter 
diameter = 2 * radius

#now display the diameter with one decimal place 
print(f"The diameter of the circle is {diameter:.1f}\n")

#calcualte the circumfrance 
circumfrance = 2 * math.pi * radius

#now display the circumfrance with two decimal places
print(f"The circumfrance of the circle is {circumfrance:.2f}\n")

#calculate the area
area = math.pi * radius ** 2

#now display the area with three decimal places 
print(f"The area of the circle is {area:.3f}\n")


