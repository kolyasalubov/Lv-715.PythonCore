n1 = input("Enter a string")
def characters():

    d={}
    for i in range(len(str)):
        d1={str[i]:str.count(str[i])}
        d.update(d1)
    print(d)
    
characters()