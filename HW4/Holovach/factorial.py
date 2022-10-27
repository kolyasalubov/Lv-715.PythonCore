# Factorial

border = input("Enter the max value:")

factorial = 1

for i in range(2, int(border)+1):
    factorial *=i

print(f"Factorial of {border} is equal to {factorial}!")


