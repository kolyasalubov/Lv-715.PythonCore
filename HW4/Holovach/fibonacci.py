# Fibonacci sequence

fibonacci = int(input("Enter the limit:"))

first = 0
second = 1
count = 0 

if fibonacci <= 0:
    print("Please enter a positive integer")
elif fibonacci == 1:
    print(f"Fibonacci sequence upto : {first}")
else:
    print("Fibonacci sequence:", end = ' ')
    while count < fibonacci:
        print(first, end = ' ')
        thirth = second+first
        first = second
        second = thirth
        count += 1
    

    


