# class work 3, task 1

while True:

    try:
        number1 = float(input("Please type a first number. If you want to exit, type 'exit' "))
        number2 = float(input("Please type a second number. If you want to exit, type 'exit' "))

        if number1 > number2:
            print("The first number is more then the second")
        elif number1 < number2:
            print("The first number is less then the second")
        else:
             print("Both numbers are equal")
             
    except ValueError:
        print("Incorrect characters were given")
        break