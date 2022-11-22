def day(value):
    value = int(value)
    lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return lst[value - 1]


try:
    value = input("Enter your number of the day: ")
    if int(value) <= 0 or int(value) >= 8:
        raise ValueError("Invalid number")
except ValueError as e:
    print(e)
else:
    print(day(value))
