# 
# Example file for variables
#

# Declare a variable and initialize it

b = 1
print(b)

# re-declaring the variable works
"""

b = "abed"
print(b)

# ERROR: variables of different types cannot be combined
b = 1 + "abc"
print(b)
"""

# Global vs. local variables in functions
def var():
    global b
    b = 0
    print(b)



var()
print(b)




