# Firsly, let's create a list of numbers
num_list = list(range(5))

# \\We can also prompt the user for the numbers:
#       \\We create an empty list
# num_list = []
#       \\Then we define hoe many numbers do we take from the user
#       \\We can ommit this stage and specify in the loop range(5) if needed
# list_length = 5
#       \\Then we loop the prompt and store the nums into the list
# for num in range(list_length):
#     user_num = int(input("Enter your num: "))
#     num_list.append(user_num)

# Now we want to check out list and print the type of the first item
print("The default list is: ", num_list)
print("The type of the first num is: ", type(num_list[0]))

# We convert the int type into float
num_list = [float(num) for num in num_list]

# We print out the results
print("\nThe float list will look like: ", num_list)
print("So the type of the first item is: ", type(num_list[0]))