n=int(input("Input n: "))
num_1=0
num_2=1
res=0
print('Fibonacci numbers up to the entered number %d:\n'%(n),res, sep='')
while num_2<=n:
    print(num_2)
    res=num_1+num_2
    num_1=num_2
    num_2=res