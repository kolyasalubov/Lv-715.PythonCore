user_input = input("Please enter your login : ")
while user_input != "First":
    print("\tOpps , invalid input!")
    user_input = input("Please enter again : ")
else:
    print("You have successfully logged in !")