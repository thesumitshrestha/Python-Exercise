# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

user_number = int(raw_input("Enter a number: "))
if (user_number <= 17):
    print("The user number is less than 17")
    difference_number = 17 - user_number
    print (difference_number)

else:
    print("The user number is greater than 17")
    difference_number = (user_number - 17) * 2
    print (difference_number)
