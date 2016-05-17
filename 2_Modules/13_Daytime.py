#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# --to convert from seconds to datetime use datetime.datetime.fromtimestamp() function
# --you can specify time in seconds using time.time()
# --you can specify time using datetime.datetime.now() or specifyign certain date and time
# --you can also use time delta to specify period of time datetime.timedelta()
# --you can do your own time formatting with stftime()
# oct21st.strftime("%B of '%y")
# --you can also convert your own strings into the datetime object using strptime()
# datetime.datetime.strptime("November of '63", "%B of '%y")
# %Y - Year with century, as in '2014'
# %y - Year without century, '00' to '99'(1970 to 2069)
# %m - Month as a decimal number, '01' to '12'
# %B - Full month name, as in 'November'
# %b - Abbreviated monthname, as in 'Nov'
# %d - Day of the month, '01' to '31'
# %j - Day of the year, '001' to '366'
# %w - Day of the week, '0'(Sunday) to '6'(Saturday)
# %A -  Full weekday name, as in 'Monday'
# %a - Abbreviated weekday name, as in 'Mon'
# %H - Hour(24 - hour clock), '00' to '23'
# %I - Hour(12 - hour clock), '01' to '12'
# %M - Minute, '00'to '59'
# %S - Second, '00' to '59'
# %p - 'AM' or 'PM'
# %% - Literal '%' character

import datetime, time

print(datetime.datetime.now())

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year)
print(dt.month)
print(dt.day, dt.hour)

today = time.time()
print(datetime.datetime.fromtimestamp(today))
print('----')
# using the delta object
delta = datetime.timedelta(days=1)
print(delta.total_seconds())

# you can perform math operations on the time data
now = datetime.datetime.now()
delta = datetime.timedelta(days=1000)
print(now + delta)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))