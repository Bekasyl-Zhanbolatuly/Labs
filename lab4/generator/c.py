def it(n):
    for x in range(1, n+1):
        if x%12== 0:
            yield x
        else:
            continue
n = int(input())
print(*it(n), sep=', ')