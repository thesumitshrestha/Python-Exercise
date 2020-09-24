# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = raw_input("Enter comma separated numbers: ")
list = numbers.split(',')
tuples = tuple(list)
print "The list is: " + str(list)
print "The tuple is: " + str(tuples)
