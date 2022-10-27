# class work 3, task 2

try:

    number = int(input("Type a number "))
    
    if number % 2 == 0:
        print("The given number is even")
    elif number % 2 == 1:
        print("The given number is odd")

except ValueError:
    print("Incorrect symbols were given - not a natural number")