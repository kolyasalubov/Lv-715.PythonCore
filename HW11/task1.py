def age_fun(value):
    value = int(value)
    if value % 2 == 0:
        return "The age is even"
    else:
        return "The age is odd"


try:
    value = input("Enter your age: ")
    if int(value) <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as e:
    print(e)
else:
    print(age_fun(value))
