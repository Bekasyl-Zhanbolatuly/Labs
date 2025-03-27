import datetime

yt = datetime.datetime.now() - datetime.timedelta(days=1)
tm = datetime.datetime.now() + datetime.timedelta(days=1)
td = datetime.datetime.now()

print("Yesterday:", yt.strftime("%Y-%m-%d"))
print("Today:",td.strftime("%Y-%m-%d"))
print("Tommorow:", tm.strftime("%Y-%m-%d"))