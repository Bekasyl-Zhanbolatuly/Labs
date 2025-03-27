def inv(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
a = inv(n)
while n > 0:
    print(next(a))
    n -= 1