# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.


import logging

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

try:
    user_age = int(input("Enter your age: "))
    if user_age <= 0:
        raise Exception(
            "Your age must not be a negative number and equal to 0")
except ValueError as ex:
    logging.exception(f'Value error.Info: {ex}')
except Exception as ex:
    logging.exception(f'Error Info: {ex}')
else:
    if user_age % 2 == 0:
        print("The number of your age is even")
    elif user_age % 2 != 0:
        print("The number of your age is odd")
finally:
    print("The 'try except' is finished")
