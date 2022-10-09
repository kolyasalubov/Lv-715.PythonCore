from random import randint

def guess_num():
    ''' Executes a game of guessing the num between 1 and 10000
    '''

    random_num = randint(1, 10000)
    user_num = int(input('Guess the frickin number form 1 to 10000: '))
    while user_num != random_num:
        if user_num > random_num:
            user_num = int(input('No, the num is lower. Try again: '))
        if user_num < random_num:
            user_num = int(input('No, the num is higher. Try again: '))
    
    print('You got the right num:', random_num, '!')


guess_num()


