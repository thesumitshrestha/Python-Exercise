# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user. Go to the editor

user_number = int(raw_input("Enter a number to check if it is odd or even: "))
if (user_number % 2 == 0):
    print ("You have entered an even number")

elif (user_number % 2 != 0):
    print ("You have entered an odd number")

else:
    print ("Please enter a valid number")
