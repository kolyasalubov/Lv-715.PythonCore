# class work 8, addditional task 2

from random import randint

random_number = randint(1, 101)

user_number = int(input("I have chosen some number. Let's try find out what is that :) "))

while user_number != random_number:
    if user_number > 100:
        print("My number is in range 1 and 100. Try again ")
        user_number = int(input("Let's try find out what is that :) "))
    elif user_number > random_number:
        print("My number is less then yours. Try again")
        user_number = int(input("Let's try find out what is that :) "))
    else:
        print("My number is more then yours. Try again")
        user_number = int(input("Let's try find out what is that :) "))
else:
    print("Congratulations! Your number is equal with mine. ")