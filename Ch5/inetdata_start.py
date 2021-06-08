
import urllib.request
#
# Example file for retrieving data from the internet
#
def main():
  webUrl = urllib.request.urlopen("http://www.google.com")

  # get the result code and print it
  print ("result code: " + str(webUrl.getcode()))

  print(webUrl.read())


if __name__ == "__main__":
  main()
