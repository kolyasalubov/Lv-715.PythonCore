def summation(num):
    summa = 0
    for i in range(num + 1):
        summa = summa + i
    return summa


assert summation(2) == 3
assert summation(4) == 10
assert summation(5) == 15
assert summation(8) == 36
