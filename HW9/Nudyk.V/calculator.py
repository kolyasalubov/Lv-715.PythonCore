from math_calc import *


def action():
    ''' Prompts the user for a certain actions and then calculates the action between
        the two given numbers. Need to import functions from math_calc
    '''
    
    user_input = input('What do you want to do?:\n \
    - 1 for adding\n \
    - 2 for deducting\n \
    - 3 for mulpiplying\n \
    - 4 for dividing:\n')

    user_num = int(input('Enter first number: '))
    user_num2 = int(input('Enter second number: '))

    match user_input:
        case '1':
            print(adding(user_num, user_num2))
        case '2':
            print(substract(user_num, user_num2))
        case '3':
            print(multiply(user_num, user_num2))
        case '4':
            print(divide(user_num, user_num2))



action()
