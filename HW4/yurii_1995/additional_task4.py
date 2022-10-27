# class work 4, task 4 (using continue statement)

odd_numbers = []

for number in range(1, 100):
    if number % 2 == 0:
        continue
    else:
        odd_numbers.append(number)

print(odd_numbers)

# class work 4, task 4 (without continue statement)

odd_numbers_2 = []

number = 0

while number < 100:
    number += 1
    if number % 2 == 1:
        odd_numbers_2.append(number)
    else:
        pass

print(odd_numbers_2)