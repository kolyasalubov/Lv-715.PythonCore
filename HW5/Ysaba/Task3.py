#HW5 , task 3
#Fibonacci sequence up to n-th term
n1 = 0
n2 = 1
count = 0
amount = int(input("Enter a number of elements in Fibonacci sequence : "))
print(f"{amount} elements in Fibonacci sequence : ")
while count < amount:
    print(n1 , end =' ')
    result = n1 + n2
    n1 = n2
    n2 = result
    count +=1