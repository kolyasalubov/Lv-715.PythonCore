number = int(input("Print number = "))
factorial = 1

while number > 1:
    factorial = number * factorial
    number = number - 1
print(f"factorial = {factorial}")