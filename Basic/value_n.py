# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(raw_input("Enter an integer: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
number = n1 + n2 + n3
print("The value of n is: " + str(number))
