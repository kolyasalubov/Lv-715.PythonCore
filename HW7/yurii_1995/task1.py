# home work 7, task 1

from random import randint

def get_largest_number(first_number, second_number):
    """This function recognizes and returns a largest number from input two numbers.
    The input data can be int or float types. 
    """

    if first_number > second_number:
        return first_number
    else:
        return second_number

first_number = randint(1, 1000)
second_number = randint(1, 1000)

print(f"The first number is {first_number}")
print(f"The second number is {second_number}")
print(f"The largest number is {get_largest_number(first_number, second_number)}")