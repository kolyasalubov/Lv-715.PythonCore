lst_number = []


def valid_input(x):
    if not x.isdigit():
        return True


def guess_number(x):
    if x not in lst_number:
        lst_number.append(x)
    else:
        return True


def game():
    import random

    number = random.randint(0, 100)
    guesses = 10
    while True:
        user_number = input("Enter number: ")
        if valid_input(user_number):
            print("You have entered wrong value! Please enter number between 0 - 100")
            continue
        user_number = int(user_number)
        if guess_number(user_number):
            print("you have already enter this number")
            continue
        if user_number > number:
            guesses -= 1
            print("the number is smaller")
            print(f"you have {guesses} guesses left")
        if user_number < number:
            guesses -= 1
            print("the number is bigger")
            print(f"you have {guesses} guesses left")
        if guesses == 0:
            print(f"You are out of guesses, number was: {number}")
            break
        if user_number == number:
            print("Well done!")
            break


game()
