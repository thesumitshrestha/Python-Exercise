# Write a Python program to count the number 4 in a given list.

def count_of_4(nums):
    count = 0
    for num in nums:
        if (num == 4):
            count = count + 1

    return count


print("The count of 4 is " + str(count_of_4([2, 3, 4, 5, 4, 44, 4, 24, 6])))
