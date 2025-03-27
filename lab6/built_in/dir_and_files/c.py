import os

pat = input("Input path: ")
if os.path.exists(pat):
    print("The path exists")
    dir = os.path.dirname(pat)
    file = os.path.basename(pat)
    print(dir)
    print(file)
else:
    print("The path does not exist")