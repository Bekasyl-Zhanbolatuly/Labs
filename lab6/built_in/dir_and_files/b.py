import os

pat = input("Input path: ")

if os.path.exists(pat):
    print("The path exists")

    if os.path.isfile(pat):
        print("It's a file.")
    elif os.path.isdir(pat):
        print("It's a directory.")

    print("Readable" if os.access(pat, os.R_OK) else "Unreadable")
    print("Writable" if os.access(pat, os.W_OK) else "Unwritable")
    print("Executable" if os.access(pat, os.X_OK) else "Unexecutable")
else:
    print("The path does not exist")
