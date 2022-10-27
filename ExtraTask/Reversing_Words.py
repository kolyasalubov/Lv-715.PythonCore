def reversing(s):
    return s[::-1]


word = "Hi There."
lst = word.split()
result = " ".join(reversing(lst))
print(result)

