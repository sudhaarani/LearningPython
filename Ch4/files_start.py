#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("egfile.txt", "w+")
  
  # Open the file for appending text to the end
  f = open("egfile.txt", "r")

  # write some lines of data to the file
  # f.write("this is a line \n")
  
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    contents = f.read()
    print(contents)

    
if __name__ == "__main__":
  main()
