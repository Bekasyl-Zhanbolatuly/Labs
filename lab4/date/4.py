import datetime

n = 2
while n > 0:
    y = int(input("Year: "))
    m = int(input("Month: "))
    d = int(input("Day: "))
    h = int(input("Hour: "))
    m1 = int(input("Minute: "))
    s = int(input("Second: "))
    global date1, date2
    if n == 2:
        date1 = datetime.datetime(y, m, d, h, m1, s)
    else:
        date2 = datetime.datetime(y, m, d, h,m1,s)
    n -= 1
dif = date2 - date1
dfs = dif.total_seconds()
print(dfs)