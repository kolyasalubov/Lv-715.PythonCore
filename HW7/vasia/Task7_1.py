def larger_number(num1,num2):
    '''
    Function return the largest number of two numbers 
    '''
    if num1>num2:
        print(f"{num1} larger than {num2}.")
        return num1
    elif num2>num1:
        print(f"{num2} larger than {num1}.")
        return num2
    else: 
        print("The numbers are equal.")
        return num1

print(larger_number(10,10))