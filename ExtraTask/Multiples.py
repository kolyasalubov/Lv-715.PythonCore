def Multiples(n):
    if n < 0:
        return 0
    else:
        sum = 0
        for i in range(0, n):
            if i % 5 == 0 or i % 3 == 0:
                sum += i
        return sum


print(Multiples(10))
