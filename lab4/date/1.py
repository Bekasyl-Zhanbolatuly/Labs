import datetime

cur = datetime.datetime.now()
delt = datetime.timedelta(days=5)
goal = cur - delt
print(goal)