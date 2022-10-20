import random
random_value = random.randint(0,101)

for k in range (0,101):
    value = int(input('your number = '))
    while value != random_value:
        if value > random_value:
            print ('input lower number')
            break
        elif value < random_value:
            print ('input higher number')
            break
    else:
        print('well done')
        break