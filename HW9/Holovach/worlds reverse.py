def reverse(st):
    st = list(st.split())
    st.reverse()
    st = " ".join(st)
    # st = " ".join(list(st.split()).reverse())
    return st

print(reverse("hjgffg kjhkjh"))