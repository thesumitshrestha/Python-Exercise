# Write a Python program to create a histogram from a given list of integers

def histogram(list):
    for n in list:
        output = ''
        times = n
        while (times > 0):
            output += '*'
            times = times - 1
        print(output)


histogram([2, 3, 4, 5])
