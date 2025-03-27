st = input("Write a word: ").lower()
strev = st[::-1]

if st == strev:
    print("Word is palindrome")
else:
    print("Word is not palindrome")