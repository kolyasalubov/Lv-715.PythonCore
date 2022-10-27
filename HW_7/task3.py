a = "Hello"
result = {}
for i in a:
    if i not in result:
        result[i] = 0
    result[i] = result[i] + 1
print(result)

