import datetime

today = datetime.datetime.today()
print("Today is     ",today.strftime("%d/%b/%Y %H:%M:%S"))
yesterday = today-datetime.timedelta(days=1)
print("Yesterday is ",yesterday)
tomorrow = today+datetime.timedelta(days=1)
print("Tomorrow is  ",tomorrow)