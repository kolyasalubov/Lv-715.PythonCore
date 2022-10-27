# Multiples of 3 or 5

def solution(number):
    numbers = range(0, number)
    sum = 0
    
    if number < 0:
        return 0
    else:
        for digit in numbers:
            if digit % 3 == 0:
                sum = digit + sum
            elif digit % 5 == 0:
                sum = digit + sum
            else:
                continue
    return sum