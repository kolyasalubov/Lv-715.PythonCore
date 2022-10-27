#HW4 ,task 1
number = int(input("Enter a number : "))
result = 1
if number == 1:
    print(f"The factorial of {number} is 1 ")
elif number < 0:
    print(f"You can't calculate factorial of {number}")
else:
    for x in range(1,number + 1 ):
        result = result * x
    print(f"The factorial of {number}  is {result}")