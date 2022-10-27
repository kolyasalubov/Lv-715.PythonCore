numder = input("Введіть 4 числа: ")
Product = int(numder[0]) * int(numder[1]) * int(numder[2]) * int(numder[3])
print("Добуток числа:  ", Product)
print(f"Число наоборот:  {numder[3]}{numder[2]}{numder[1]}{numder[0]}")
print("Відсуртовано:  ", numder[0], numder[1], numder[2], numder[3])
reverse = list(numder)
reverse = sorted(reverse)

