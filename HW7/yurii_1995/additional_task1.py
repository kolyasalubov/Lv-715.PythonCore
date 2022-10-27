# class work 7, task 1

def calculate_arithmetic_mean(*args: int) -> int:
    """This function accepts any count of numbers and returns the arithmetic mean of them"""

    sum = 0

    for number in args:
        sum += number

    return round(sum / len(args))

print(calculate_arithmetic_mean(56, 78, 5, 7, 8, 456)) # example. Result is 102