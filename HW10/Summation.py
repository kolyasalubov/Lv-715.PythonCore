def summation(num):
    
    sum = 0
    for number in range(1, num + 1):
        sum += number
    return sum


print(summation(9))