#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now=datetime.now()

  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("year : %y"))
  print(now.strftime("weekday : %a"))
  print(now.strftime("month : %b"))
  print(now.strftime("day : %d"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("locale date  nd year : %c"))
  print(now.strftime("locale date : %x"))
  print(now.strftime("locale time : %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime(" time : %I:%M:%S %p"))


if __name__ == "__main__":
  main();
