
import calculator as c

first_number = int(input("Enter first number:"))

operation = input("Choose operition's type( +, -, /, * ):")

second_number = int(input("Enter second number:"))

def operate(first_number, operation, second_number):

    match operation:
        case "+":
            return c.sum(first_number,second_number)
        case "-":
            return c.sub(first_number,second_number)
        case "*":
            return c.mult(first_number,second_number)
        case "/":
            return c.dev(first_number,second_number)
        case _:
            print("Choose correct operation's type!")
            return False


print(operate(first_number, operation, second_number))
