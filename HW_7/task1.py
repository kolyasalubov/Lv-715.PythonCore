def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


assert max_of_two(10, 20) == 20
assert max_of_two(100, 20) == 100
assert max_of_two(100, 100) == 100
assert max_of_two(-1, 3) == 3
