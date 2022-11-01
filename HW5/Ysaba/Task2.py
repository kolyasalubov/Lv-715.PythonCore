# You can get user input from keybord.
list_of_numbers1 = input("Enter some numbers using space between them : ")
list_of_numbers2 = list_of_numbers1.split()
new_list  = []
for i in list_of_numbers2:
    new_list.append((float(i)))
print(new_list)


#Here we have list that already contains elements of integer type.
list_of_numbers = [3,4,8,821,41,6,198,3781,1214]
new_list  = []
for i in list_of_numbers:
    new_list.append((float(i)))
print(new_list)