range_length = int(input("Enter element's number:"))

list_for_checking = []


for x in range(range_length):
    list_for_checking.append(int(input(f"Enter elment № {x}: ")))


for y in list_for_checking:
    if y%2 != 0:
        print(f"Odd ({y}) has been found!")
        break
else:
    print("Odd hasn't been found!")
