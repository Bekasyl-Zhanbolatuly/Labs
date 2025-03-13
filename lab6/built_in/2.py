st = str(input())

def let(s):
    up =0
    low = 0
    for x in s:
        if x.isupper():
            up += 1
        elif x.islower():
            low += 1
    return up,low
upp, loww = let(st)
print(f"Uppercase leters: {upp}")
print(f"Lowwercase leters: {loww}")