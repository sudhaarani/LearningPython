#
# Example file for working with functions
#

# define a basic function
def f1():
    print("function 1")
    # return 1


# function that takes arguments
def f2(arg1 , arg2 = 1):
    sum = arg1 +arg2
    return sum

# function that returns a value
def f3(x):

    return x*x


# function with default value for an argument
# addition of same value repeated times based on arg2s
def f4(arg1 , arg2 = 3):
    r = 0
    print(range(arg2))
    for i in range(arg2):
        r += arg1
    return r



#function with variable number of arguments
def f5(*args):
    # r = 1
    for i in args:
        print(i)

#
f1()
# print(f1())
# print(f1)

a = f2(1)
a = f2(a , a)
print(a)
# print(f3(10))
# print(f4(2))
# f5(1, 2, 3)


