import datetime

now= str(datetime.datetime.now().astimezone() - datetime.timedelta(hours=9)).split()
now1 = now[0].split("-")

for i in now1:
    print(i)