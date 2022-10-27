# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.

# def greet(name):
#     return "Hello, {name}!".format(name=name)
#     if name == "Johnny":
#         return "Hello, my love!"

# After the first return the code stopped running
# We can rewrite it as a if/else consition
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


print(greet("you"), greet("Johnny"))


# Or a one-liner
def greet_v2(name):
    return ('Hello, my love!' if name == 'Johnny' else (f'Hello, {name}!'))


print(greet_v2('you'), greet_v2('Johnny'))