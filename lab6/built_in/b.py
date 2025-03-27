st = input()

def let(s):
    up = 0
    low = 0
    for x in s:
        if x.isupper():
            up += 1
        elif x.islower():
            low += 1
    return up, low

upp, loww = let(st)
print(f"Uppercase letters: {upp}")
print(f"Lowercase letters: {loww}")