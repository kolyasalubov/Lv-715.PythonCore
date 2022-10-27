def filter_words(st):
    x = st.capitalize()
    x = x.strip()

    sentance = []

    for y in range(len(x)):
        if x[y] == ' ' and x[y+1] == ' ':
            continue
        sentance.append(x[y])
    
    return ''.join(sentance)

print(filter_words("HGFHF   GJHGJxcv    KHBKJBJKGK    HBGBL"))

def filter_words_hack(st):
    return st.capitalize().split()
    # return ' '.join(st.capitalize().split())

print(filter_words_hack("HGFHF   GJHGJxcv    KHBKJBJKGK    HBGBL"))