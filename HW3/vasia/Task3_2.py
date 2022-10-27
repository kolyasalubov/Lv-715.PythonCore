Number=9281
Number_str=str(Number)
print("Task2_1")
res=1
for i in range (len(Number_str)):
    res*= int(Number_str[i])
print("The result is:",res)
print("Task2_2")
res=''
for i in range (len(Number_str),0,-1):
    res+=Number_str[i-1]
Number_reverse= int(res)
print("The reverse number is:",Number_reverse)
print("Task2_3")
res=''
for i in range (10):
    for j in range(len(Number_str)):
        if int(Number_str[j])==i:
            res+= Number_str[j]
print("The result is:",res)
    