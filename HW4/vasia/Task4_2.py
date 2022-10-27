#Task without input

lst=[2,3,10,-1, 2568, 0]
print("List that contains elements of integer type: ",lst)
for i in range(len(lst)):
    lst[i]=float(lst[i])
print("List that contains elements of float type: ",lst)


#Task with input and using method list.append

# lst=[]
# n=int(input("Enter the number of list items:"))
# for i in range(n):
#     num = int(input("Enter %d element: "%(i)))
#     lst.append(num)
# print("List that contains elements of integer type:",lst)
# for i in range(len(lst)):
#     lst[i]=float(lst[i])
# print("List that contains elements of float type: ",lst)
