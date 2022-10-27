def banjo(name):
    if name[0] == 'r' or name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


name = input("Enter name: ")
print(banjo(name=name))
