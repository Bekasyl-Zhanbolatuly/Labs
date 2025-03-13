def squares(a, b):
    for x in range(a, b+1):
        yield x**2
a = int(input())
b = int(input())
n = squares(a, b)
for sq in n:
    print(sq)