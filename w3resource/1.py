# Write a Python program to display the current date and time.
import datetime

now = datetime.datetime.now()
print ("Current date and time is " + str(now))
print ("Current date and time after formatting is " + now.strftime("%Y-%m-%d %H:%M:%S"))
