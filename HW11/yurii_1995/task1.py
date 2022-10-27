# home work 11, task 1

def determine_age(user_age) -> str:
    """This function displays a message stating whether the age is even or odd"""
    if user_age % 2 == 1:
        return "Your age is odd"
    else:
        return "Your age is even"

try:
    user_age = int(input("Enter your age: "))
    if user_age == 0:
        raise ValueError("Your age can't be equil to zero")
    elif user_age < 0:
        raise ValueError("Your age can't be a negative number")
    else:
        result = determine_age(user_age)
        print(result)
except ValueError as e:
    print(e)
