#############
## Types
#############
# Check types with:
# type()
# Characters and strings are enclosed in '' or ""
type("This is a string") # string
type(3) # int
type(3.14) # float
type(True) # bool (logical True or False)

# You can also force types by calling the type as a function
int(True) # 1
int(False) # 0
str(330)
type(330)
# Functions can be nested in other functions, more on this later
type(str(330))
