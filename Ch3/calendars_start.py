#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
p = c.formatmonth(2021, 5)
print("calender of may month" , p)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar()
p = hc.formatmonth(2021, 5)
print("calender of may month in html" , p)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021,5):
    print(i)

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("nmes of dys ")

for day in calendar.day_name:
    print(day)

print("nmes of months")
for month in calendar.month_name:
    print(month)


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("  team meeting on")
for m in range(1,13):
    cal= calendar.monthcalendar(2021, m)
    # print(cal)
    weekone= cal[0]
    weektwo= cal[1]

    if weekone[calendar.FRIDAY] == 0:
        meetday= weektwo[calendar.FRIDAY]
    else:
        meetday= weekone[calendar.FRIDAY]

    print(calendar.month_name[m],meetday)