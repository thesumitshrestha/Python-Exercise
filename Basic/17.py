#Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_number(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(near_number(123))
print(near_number(900))
print(near_number(1501))
print(near_number(1499))
