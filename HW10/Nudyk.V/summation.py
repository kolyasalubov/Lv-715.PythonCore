# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.


def summation(num):
    '''
    Returns a sum of all the nums in range for 1 to the given number
    '''
    
    sum = 0
    for number in range(1, num + 1):
        sum += number
    return sum


print(summation(10))