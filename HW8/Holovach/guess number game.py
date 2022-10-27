import random

def game():

    attempts_number = int(input("How many atttempts do you need to guess set number?:"))

    set_number = random.randint(1,100)

    while attempts_number > 0:

        attempt = int(input("Enter your number:"))

        if attempt == set_number:
            print("You win!!")
            break
        else:
            if attempt > set_number:
                print("Your number is bigger")
            else:
                print("Your number is lowwer")

        attempts_number -= 1  
 
        print(f"You have {attempts_number} attempts yet")
    else:
        print("Your attempts are ended. You didn't guess!")

game()