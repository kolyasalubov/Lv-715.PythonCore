# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону
# чисел від 1 до 100 і пропонує користувачу вгадати це число.

# Програма зчитує числа, які вводить користувач і видає користувачу підказки
# про те чи загадане число більше чи менше за введене користувачем.
# Гра має тривати до моменту поки користувач не введе число, яке загадане
# програмою, тоді друкує повідомлення привітання.
# (для виконання завдання необхідно імпортувати модуль random, а з нього
#  функцію randint())

from random import randint

user_num = int(input(
    '''Welcome to the game "Guess the number! You will try to guess a random number 
between 1 and 100. Let's do it. Enter a number:  '''))

secret_num = randint(1, 100)


while user_num != secret_num:
    if 1 > user_num or user_num > 100:
        print("Oops! Your number doesn't range from 1 to 100. Try again.")
        user_num = int(input('Enter a new number: '))
    elif secret_num > user_num:
        print('Your number is less than the secret number. Try again.')
        user_num = int(input('Enter a new number: '))
    elif secret_num < user_num:
        print('Your number is bigger than the secret number. Try again.')
        user_num = int(input('Enter a new number: '))

if secret_num == user_num:
    print('Congrad. You win!')
