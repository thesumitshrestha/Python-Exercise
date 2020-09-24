# Write a Python program to calculate number of days between two dates.

from datetime import date

f_date = date(2020, 10, 2)
l_date = date(2020, 10, 8)
delta = l_date - f_date
print (delta.days)
