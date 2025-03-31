import datetime
mytime = datetime.time(2,20, 1, 30)
print(mytime)
print(mytime.hour)
print(mytime.minute)
print(mytime.microsecond)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print(today.ctime())

from datetime import datetime
mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2030)
print(mydatetime)

from datetime import date

date1 = date(2030, 11, 3)
date2 = date(2020, 11, 3)
result = date2 - date1
print(result.days)
