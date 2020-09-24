# Write a Python program to accept a filename from the user and print the extension of that.

file_name = raw_input("Enter a filename with extension: ")
file_extenstion = file_name.split('.')
print ("The extension of file " + file_name + " is " + file_extenstion[-1])
