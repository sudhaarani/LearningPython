#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():

  # DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today= date.today()
  print("today :", today)

  # print out the date's individual components
  print("individual comp :", today.day , today.month, today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("weekday ", today.weekday())
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  print("weekday ", days[today.weekday()])


  print("Tomorrow will be " + days[(today.weekday() + 1)%7])
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print("today :", datetime.today())
  
  # Get the current time

  print("today current time :", datetime.time(datetime.now()))
 

  
if __name__ == "__main__":
  main();
  