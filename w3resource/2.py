# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def diff(data):
    if len(data) == len(set(data)):
        print (len(data))
        print (len(set(data)))
        return True
    else:
        return False


print(diff([2, 3, 4, 4, 5, 6, 7]))
