import os
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%root)
print("-"*40)
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%root)
    print("%s"%files)
print("-"*40)
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%files)