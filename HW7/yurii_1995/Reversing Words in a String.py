# Reversing Words in a String

def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    
    return st

print(reverse("Hello World"))