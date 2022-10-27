factorial = int(input("Введіть факторіал: "))
num1 = 1
for i in range(2, factorial+1):
    num1 = num1 * i
print("Результат: ", num1)