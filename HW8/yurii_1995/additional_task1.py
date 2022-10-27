# class work 8, addditional task 1

import calculator

user_number_1 = int(input("Please type your first number: "))
user_number_2 = int(input("Please type your second number: "))
user_choice = input("What would you like to do with your numbers? (+, -, *, / ")

if user_choice == "+":
    print(calculator.get_sum(user_number_1, user_number_2))
elif user_choice == "-":
    print(calculator.get_diffirence(user_number_1, user_number_2))
elif user_choice == "*":
    print(calculator.get_product(user_number_1, user_number_2))
elif user_choice == "/":
    print(calculator.get_division(user_number_1, user_number_2))
else:
    print("You must type a correct operator, something like that: +, -, * or / !")