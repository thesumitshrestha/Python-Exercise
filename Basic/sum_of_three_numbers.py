# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

n1 = int(raw_input("Enter first number: "))
n2 = int(raw_input("Enter second number: "))
n3 = int(raw_input("Enter third number: "))


def sum(n1, n2, n3):
    if (n1 == n2 == n3):
        n = n1 + n2 + n3
        n = n * 3
        return n
    else:
        n = n1 + n2 + n3
        return n


print (sum(n1, n2, n3))
