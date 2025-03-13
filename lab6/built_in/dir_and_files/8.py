import os

pat = input("Input path: ")
if os.path.exists(pat):
    print("The path exists")
    if os.access(pat, os.R_OK):
        print("Readable")
    else:
        print("Unreadable")
    if os.access(pat, os.W_OK):
        print("Writable")
    else:
        print("Unwritable")
    if os.access(pat, os.X_OK):
        print("Executable")
    else:
        print("Unexecutable")
    os.remove(pat)
else:
    print("The path does not exist")