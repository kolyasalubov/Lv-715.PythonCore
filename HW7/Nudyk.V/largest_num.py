# Write a function that returns the largest number of two numbers

# In this version we don't have to return the values
# Also we can write everything in the func and just execute it at the end
def largest_num():
    '''Takes two numbers from the user and returns the largest'''

    print(largest_num.__doc__)

    user_num1 = input('Enter the first number: ')
    user_num2 = input('Enter the first number: ')
    if user_num1 > user_num2:
        print(f'{user_num1} is larger!')
    elif user_num2 > user_num1:
        print(f'{user_num2} is larger!')
    else:
        print('The numbers are equal!')


largest_num()


# Second version

# In this version the func is specefically for comparing nums
user_num1_1 = input('Enter the first number: ')
user_num2_2 = input('Enter the first number: ')

def largest_num_v2(num1, num2):
    '''Takes two numbers from the user and returns the largest'''

    if num1 > num2:
        return (f'{num1} is larger!')
    elif num2 > num1:
        return (f'{num2} is larger!')
    else:
        return ('The numbers are equal!')


print(largest_num_v2.__doc__)
print(largest_num_v2(user_num1_1, user_num2_2))


