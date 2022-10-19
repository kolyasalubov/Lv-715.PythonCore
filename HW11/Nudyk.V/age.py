def odd_or_even(number):
    '''
    Checks if the given muber is even or odd
    '''
    if number % 2 == 1:
        print('The num is odd')
    else: 
        print('The num is even')


try:
    age = int(input('Enter your age: '))
    if age < 0:
        raise ValueError("The age cannot be a negative number")
    odd_or_even(age)  
except ValueError as e:
    print(e)