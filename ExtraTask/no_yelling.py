
def filter_words(words):
    kol = 0
    result = ""
    for i in range(len(words)):
        if words[i] == " ":
            kol += 1
        else:
            kol = 0
        if kol > 1:
            continue
        result += words[i]
    print(result.capitalize())

filter_words('HELLO     CAN YOU HEAR        ME')