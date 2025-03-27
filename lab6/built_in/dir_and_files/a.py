import os

path = r"C:\Users\ADMIN\Git labs\Labs\lab4"  
if not os.path.exists(path):
    print(f"Папка '{path}' не найдена.")
else:
    for (root, dirs, files) in os.walk(path):
        print("%s" % root)
    print("-" * 40)

    for (root, dirs, files) in os.walk(path):
        print("%s" % root)
        print("%s" % files)
    print("-" * 40)

    for (root, dirs, files) in os.walk(path):
        print("%s" % files)
