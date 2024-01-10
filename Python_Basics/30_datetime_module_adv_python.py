import datetime as dt 
import pytz

'''
useful links
Datetime - https://docs.python.org/3/library/datetime.html
Pytz - https://pypi.org/project/pytz/
'''

# there are two types naive and aware

print(dt.date(2024, 1, 10)) # enter as simple integer don't enter 1 as 01

today_date = dt.date.today()
print(today_date)
bday_date = dt.date(2024, 7, 24)
till_date = bday_date - today_date
# till date will give time delta. difference between two dates
print(till_date)
# to access only day's 
print(till_date.days)
print(till_date.total_seconds())

time_delta = dt.timedelta(days=7)
print(time_delta)
print(today_date+time_delta, "\t", today_date-time_delta, "\t", today_date+(7*time_delta))

print()

# tillnow we worked with date. to work with time...

print(dt.time(12, 34, 21, 123453)) # inputted in the format, Hours, minutes, seconds and microseconds

# usually we dont work with time and date separately so to combine them into one....
print()
print(dt.datetime(2024, 1, 10, 8, 38, 40, 109324))
print(dt.datetime.today().date()) # to access only date
print(dt.datetime.today().time()) # to access only time

# till now all these are naive, and are not aware of timezone. before that...
print()
# first two produce similar results, and last one produces utc time
# in first two, today() doesn't allow us to specifiy timezone, where now() allows us to. so better to use now rather than today. utcnow is not used that much ig.
print(dt.datetime.today())
print(dt.datetime.now())
# print(dt.datetime.utcnow())

# to work with time zone pytz module is used rather than timezn method in datetime module
print()
india_tz = pytz.timezone('Asia/Kolkata')
# print([time for time in pytz.all_timezones if time[:4] == "Asia"])
print(india_tz)
# to localise naive datetime into aware time, there are two waya
# localize()
india_time = india_tz.localize(dt.datetime.now())
print(india_time)
print()
# astimezone
india_time = dt.datetime.now().astimezone(india_tz) # this looks better for me
print(india_time)
print()
# to make the datetim in readble format we can convert t using stftime()
fmt = "%b %d, %Y - %H:%M UTC %z Hours "
print(india_time.strftime(fmt))
# strptime converts string to time