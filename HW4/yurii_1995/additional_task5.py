# class work 4, task 5

numbers = [2, 6, 7, 45, 68, 34, 12, 89, 78]

for number in numbers:
    if number % 2 == 0:
        continue
    else:
        print(f"The list has at least one odd number - {number}")
        break