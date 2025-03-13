st = str(input("Write a word: "))
st.lower()
strev = st[::-1]
strev.lower()
if st == strev :
    print("Word is palindrome")
else:
    print("Word is not palindrome")