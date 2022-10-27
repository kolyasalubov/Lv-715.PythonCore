#Home_Work6_Task_1 ("Collection" Slide 39)

#Create list in the range from 1 to 10 
lst=[ i for i in range(1,11) ]

lst_even=[]
lst_odd=[]
lst_of_others=[]

for i in lst:
    if i%2==0:
        lst_even.append(i)
    elif i%3==0 and i%2==1:
        lst_odd.append(i)
    else:
        lst_of_others.append(i)

print("Even numbers that are divisible by 2: ",lst_even)
print("Odd numbers, which are divisible by 3: ",lst_odd)
print("Numbers that are not divisible by 2 and 3: ",lst_of_others)