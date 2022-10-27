# class work 11, task 1

try:
    def validation_number(user_number: int) -> str:
        """This function prompts the user to enter an integer and determines whether the number is even or odd"""
        if user_number % 2 == 1:
            return "Your number is odd"
        else:
            return "Your number is even"

    user_number = int(input("Type your number to check if its even or odd: "))
    print(validation_number(user_number))
except ValueError:
    print(f"You have typed incorrect data")
