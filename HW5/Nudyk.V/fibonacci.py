# We will ask the user for an int that should be the ceiling for the list
num_ceiling = int(input("Please enter your number: "))

# Now we define the beginning of the sequence 
first_num = 0
second_num = 1

# Now we define the array with the first two numbers
fibonacci_list = [0, 1]

# Now we create a loop to calculate the next num and add to the list
while first_num + second_num < num_ceiling:
    num = first_num + second_num      # calculated the next num
    first_num = second_num            # updated the first num by one
    second_num = num                  # update the second num by one
    fibonacci_list.append(num)        # updated the list

# Print out the result
print("The sequnce is: ")
print(*fibonacci_list, sep =',')