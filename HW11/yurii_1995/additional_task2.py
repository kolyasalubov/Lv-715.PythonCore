# class work 11, task 2

def division_numbers() -> float:
    """This function calculates the divide of two numbers entered by the user sequentially through a comma"""
    user_numbers = input("Type your numbers here but sequentially through a comma: ")
    user_numbers_sep = user_numbers.split(sep=",")
    if len(user_numbers_sep) == 2:
        number1 = int(user_numbers_sep[0])
        number2 = int(user_numbers_sep[1])
        result = number1 / number2
        return round(result, 2)
    else:
        return "You have typed not enough or too many numbers or not numbers as well!"

try:
    result_for_user = division_numbers()
except ZeroDivisionError as e:
    print(f"Some error occured: {e}")
except SyntaxError as e:
    print(f"Some error occured: {e}")
except ValueError as e:
    print(f"Some error occured: {e}")
except:
    print(f"Some unknown error occurred")
else:
    print(f"The result of dividing the given numbers is: {result_for_user}")
finally:
    print("All program process are closed.")
