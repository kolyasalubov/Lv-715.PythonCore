# home work 4, task 1

def factorial(number: int):
    """
    This function calculates a factorial of natural numbers. 
    Factorial of number is a product of all numbers in range between 1 and the given number.
    """

    numbers = range(1, number+1)
    number_factorial = 1 # start value

    for n in numbers:
        number_factorial = n * number_factorial
        n += 1
    
    return number_factorial

given_number = int(input("Type a number "))

print(factorial(given_number))