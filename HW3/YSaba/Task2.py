HW2, task 2.

#task 2.1
number = int(input("Enter a 4-digit number: "))
n1 = number % 10
n2 = (number // 10) % 10
n3 = (number // 100) % 10
n4 = (number // 1000) % 10
print("Result : " ,n1*n2*n3*n4)

#task 2.2
number = str(input("Enter a number : "))
print(number[::-1])

# task 2.3
number = list((input("Enter a number : ")))
print(sorted(number))