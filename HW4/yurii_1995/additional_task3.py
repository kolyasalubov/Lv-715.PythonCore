# class work 4, task 3 (using while loop)

number = 0

even_numbers = []
odd_numbers = []

while number <= 98:
    number +=1
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers)

# class work 4, task 3 (using for loop)

even_numbers_2 = []
odd_numbers_2 = []

for number in range(1, 100):
    if number % 2 == 0:
        even_numbers_2.append(number)
    else:
        odd_numbers_2.append(number)

print(even_numbers_2)