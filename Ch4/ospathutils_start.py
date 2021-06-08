#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
 print("os namee:", os.name)
  
  # Check for item existence and type
 print("item exists:", path.exists("egfile.txt"))
 print("item is a file:", path.isfile("egfile.txt"))
 print("item is a directory:",path.isdir("egfile.txt"))
 print("has link:",path.islink("egfile.txt"))
  # Work with file paths
 print("get real path:", path.realpath("egfile.txt"))
 print("split the path from file:", path.split(path.realpath("egfile.txt")))
  
  # Get the modification time
 t=time.ctime(path.getmtime("egfile.txt"))
 print("file modified time:",t)
 print(":",datetime.datetime.fromtimestamp(path.getmtime("egfile.txt")))

  
  # Calculate how long ago the item was modified
 diff= datetime.datetime.now()- datetime.datetime.fromtimestamp(path.getmtime("egfile.txt"))
 print("the item was modified since "+str(diff)+ " hours ago")
  
if __name__ == "__main__":
  main()
