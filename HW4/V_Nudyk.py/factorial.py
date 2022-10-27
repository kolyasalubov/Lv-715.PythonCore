#First we prompt the User for an integer and store it
user_number = int(input("Enter num: "))

#Create a loop to multiply each element 
for num in range(1, user_number):
    user_number = num * user_number

#Print out the result
print(f"Your numbers factorial is: {user_number}")