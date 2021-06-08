#
# Example file for working with classes
#


class class1:

    def m1(self):
        print("class1 m1")

    def m2(self, str):
        print("class1 m2 " + str)


class class2(class1):

    def m1(self):
        class1.m1(self)
        print("class2 m1")

    def m2(self, str):
        print("class2 m2 " + str)


def main():
    c = class1()
    c.m1()
    c.m2("dhaarani")

    cc = class2()
    cc.m1()
    cc.m2("dhaarani")




if __name__ == "__main__":
    main()
