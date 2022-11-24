def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    
    
    return st

print(reverse("Hello Worls"))