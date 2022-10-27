def solution(number):

    if number < 0:
        return 0

    sum = 0

    for x in range(number):
        if x%3 == 0 or x%5 == 0:
            sum += x

    return sum 

print(solution(100))
