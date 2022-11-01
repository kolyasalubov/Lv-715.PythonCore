num1 = []
num2 = []
num3 = []
for i in range(1,11):
    if i % 2 == 0:
        num1.append(i)
    elif i % 3 == 0:
        num2.append(i)
    else:
        num3.append(i)
print("Even numbers that are divisible by 2 :",num1)
print("Odd numbers, which are divisible by 3 :",num2)
print("Numbers that are not divisible by 2 and 3 :",num3)