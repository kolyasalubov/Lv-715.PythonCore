user_number = input("Enter a 4-digit number: ")

user_number_product = int(user_number[0]) * int(user_number[1]) * int(user_number[2]) * int(user_number[3])

print("Your number is: ", user_number)
print("The product of the numbers is: ", user_number_product)

print(f"The reversed number is: {user_number[3]}{user_number[2]}{user_number[1]}{user_number[0]}")

lets_sort = list(user_number)
lets_sort = sorted(lets_sort)

print("The numbers are sorted: ", lets_sort[0], lets_sort[1], lets_sort[2], lets_sort[3])
