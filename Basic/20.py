# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def integer_count(name, n):
    result = ''
    for i in range(n):
        result = result + name
    return result

print(integer_count('Sumit', 2))
print(integer_count('Shrestha', 3))
