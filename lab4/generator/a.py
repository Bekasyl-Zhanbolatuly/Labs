def num(n):
    for x in range(1, n+1):
        yield x**2
n = int(input())
x = num(n)
while n > 0:
    print(next(x))
    n -= 1