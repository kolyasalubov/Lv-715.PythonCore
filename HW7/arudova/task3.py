def wordcount (word):
    ''' this func returns count of words'''
    output = {}
    for k in word:
        output.update({str(k): word.count(k)})
    return output
value = input('world = ')
print (wordcount(value))