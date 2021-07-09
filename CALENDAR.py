import calendar
import datetime as dt
import time
print(calendar.calendar(2021))
print("\n")
for i in range(1,13):
 print(calendar.monthcalendar(2021,i))
print(calendar.weekheader(9))
print(calendar.weekday(2021,6,16))
print(calendar.firstweekday())
print(calendar.isleap(2000))
print(calendar.leapdays(2000,3000))
print(calendar.leapdays(2000,2100))
for j in range(5):
    print()
# datetime
print(dt.date(2021,6,16))
print(dt.datetime(2021,6,16,11,30,15))



