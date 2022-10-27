# home work 6, task 2

user_login = input("Enter your login: ")

while True:
    if user_login == "First":
        print("Hello, First!")
        break
    else:
        print("The entered login is invalid. Try again")
        user_login = input("Enter your login: ")
