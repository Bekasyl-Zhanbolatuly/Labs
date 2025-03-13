file = open("text.txt", 'w')
lst = ["cow", "horse", "sheep", "camel", "goat"]
for x in lst:
    file.write(x + "\n")
file.close()