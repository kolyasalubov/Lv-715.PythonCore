def greeting(user):
    if user == 'Johny':
        return "Hi, my darling"
    else:
        return f"Hi, {user}"


user_name = input()
print(greeting(user=user_name))
