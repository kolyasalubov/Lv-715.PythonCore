def filter_words(st):
    p= st.strip()
    d = p.replace('  ',' ')
    r = d[0].upper() + d[1::].lower()
    return r.replace('  ',' ')
print(filter_words('HHHHH    jjnfir '))