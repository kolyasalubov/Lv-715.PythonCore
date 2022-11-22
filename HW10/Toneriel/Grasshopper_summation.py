# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

def summation(num):
    '''This function finds the summation of every number from 1 to num. Returns integer.'''
    return sum([i for i in range(num+1)])


print(summation(8))
