# 
# Example file for parsing and processing JSON
#
import urllib.request
import json
import ssl

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  print(theJSON["metadata"].get("title"))

  
  # output the number of events, plus the magnitude and each event name
  print(str(theJSON["metadata"]["count"])+" events recorded")

  for i in theJSON["features"]:
      print(i["properties"]["mag"])

  # for each event, print the place where it occurred
  for i in theJSON["features"]:
      print(i["properties"]["place"])


  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
      if(i["properties"]["mag"] > 4):
          print(i["properties"]["mag"],i["properties"]["place"])


  # print only the events where at least 1 person reported feeling something
  print("felt something")
  for i in theJSON["features"]:
    # print("for loop")
      if ((i["properties"]["felt"]) != None):
          if((i["properties"]["felt"]) > 0):
              print(i["properties"]["mag"],i["properties"]["place"]," reported "+str(i["properties"]["felt"])," times ")

  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  # urlData="http://www.google.com"

  # Open the URL and read the data
  gcontext = ssl.SSLContext()
  webUrl = urllib.request.urlopen(urlData, context=gcontext)
  print ("result code: " + str(webUrl.getcode()))

  if(webUrl.getcode() == 200):
    data = webUrl.read().decode("utf-8")
    printResults(data)
  else:
    print("received error " + str(webUrl.getcode()))


if __name__ == "__main__":
  main()
