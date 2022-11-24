
from random import randint

def rand():

    number_rand = randint(1, 100)
    
    user_num = int(input('Попробуйте вгадати число від 1 до 100: '))
    
    while user_num != number_rand:
        
        if user_num > number_rand:
            user_num = int(input('Число менше, попробуйте ще раз:  '))
        
        if user_num < number_rand:
            user_num = int(input('Число більше, попробуйте ще раз:  '))
    
    print(f"Ви вгадали число", {number_rand})


rand()
