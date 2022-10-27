def define_the_largest_of_two_numbers(first: int, second: int) -> str:
    
    """
    The function returns the largest of two number,
    if they are not equal.
    """
    
    if first > second:
        return f"The largest is {first}"
    elif second > first:
        return f"The largest is {second}"
    else:
        return "They are equal"

# print(dir())
# print(define_the_largest_of_two_numbers.__doc__)

first_value = int(input("Enter the first value:"))
second_value = int(input("Enter the second value:"))


print(f"After comparison of two numbers - {define_the_largest_of_two_numbers(first_value, second_value)}")