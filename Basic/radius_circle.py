# Write a Python program which accepts the radius of a circle from the user and compute the area
import math

radius = input("Enter radius of the circle: ")
area = math.pi * radius * radius
print ("The area of the circle with radius " + str(radius) + " is " + str(area))
