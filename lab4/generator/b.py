def evens(n):
    for x in range(1, n+1):
        if x%2 == 0:
            yield x
        else:
            continue
n = int(input())
print(*evens(n), sep=', ')