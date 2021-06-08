#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while(x < 4):
  #   print(x)
  #   x = x + 1


  # define a for loop
  # for i in range(2, 6):
  #   print (i)



  # use a for loop over a collection
  name = ["suriya", "dhaarani"]
  for i in name:
    print(i)


  
  # use the break and continue statements
  for i in range(6):
    if i==4:
      break

    if i == 3:
      continue

    print(i)


  #using the enumerate() function to get index
  # for k, _ in enumerate(name): to get index alone not the value
  for k, v in enumerate(name):
    print(k)

if __name__ == "__main__":
  main()
