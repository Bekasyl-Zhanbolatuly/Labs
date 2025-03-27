path = input("Input the path to text file: ")

file = open(f"{path}", "r")
cnt = 0
for row in file:
    cnt = cnt + 1
print(cnt)
file.close()