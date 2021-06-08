#
# Example file for working with conditional statements
#


def main(x):
    # x, y = 10, 100

    # conditional flow uses if, elif, else
    for i in x:

        if i % 2 == 0:
            print("%s is even" % i)
            # break statement will break the loop
            continue

        print("%s is odd" % i)


    # conditional statements let you use "a if C else b"


if __name__ == "__main__":
    #list is used here
    main([1, 2, 3, 4])
