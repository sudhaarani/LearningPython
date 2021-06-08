#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print("", timedelta(days=365, hours=1, minutes=45,seconds=50))

# print today's date
today=date.today()
print("", str(today))

# print today's date one year from now
oneyear= str(today + timedelta(days=365))
print("one year from now:",oneyear)

# create a timedelta that uses more than one argument
weeks= str(today+timedelta(days=2, weeks=3))
print("2 dys 3 weeks later:", weeks)

# calculate the date 1 week ago, formatted as a string
past= today - timedelta(days=2 , hours=4,minutes=10)
print("going past " ,str(past))

### How many days until April Fools' Day?
today = date.today()
aprilfool = date(month=4, year=today.year, day=1 )
print("april foolday:", aprilfool)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if(today > aprilfool):
    print("april fool got over")
    afd = (today - aprilfool).days
    print("april fool day on %d days" % afd)
aprilfool = aprilfool.replace(today.year+1)

# Now calculate the amount of time until April Fool's Day
print("april fool coming on")
afd = (aprilfool - today).days
print("april foolday on next year %d dys" % afd)

# tried  exmple
today=date.today()
bday=date(today.year,1,30)
diff=(bday-today).days
print("difference 1st eg:",diff)
if diff>0:
  print("Birthday in %d days" % diff)
else:
  print("Birthday in %d days" % (diff+365))

# another way of same above exmple
# came wrong
if today > bday:
  print("bdy over")
  diff= (today-bday).days
  print("2Birthday in %d days" % diff)
else:
  print("tdy:",today)
  print("bday:",bday)
  # bday = bday.replace(today.year+1)
  print("bday:", bday)
  diff = (bday-today).days
  print("dif:",diff)
  print("2Birthday in %d days" % (diff))