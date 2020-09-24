# Write a Python program to check whether a specified value is contained in a group of values

def group_values(number):
    group = [1, 5, 8, 3]
    return number in group

print(group_values(-1))
print(group_values(3))
