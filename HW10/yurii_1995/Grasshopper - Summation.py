# Grasshopper - Summation

def summation(num):
    numbers = [num for num in range(1, num + 1)]
    sum = 0
    
    for number in numbers:
        sum += number
    return sum
    