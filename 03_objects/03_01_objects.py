############
# Objects
############

"""
We can create objects in python by storing either values, strings, or outputs from functions/operations in objects. This allows us to reuse outputs instead of retyping them. Objects can be overwritten and or nested within other objects as well. 
"""

# Store a value
x = 5
print(x)
# Perform an operation
x * 5 # does not store output into x
print(x)
# Overwrite variable with new output
x = x * 5
print(x)

y = 400 / 3
# get address in memory of the object with
id(x) # or
hex(id(x))
hex(id(y))
# You can see that each object gets an address in memory, so overwriting an object will remove its past value in memory and change its address in memory, removing its previous address.
hex(id(x))
x = x * 1000
hex(id(x))
id(y)

## Work on adding more about interning and how python associates objects in memory (WIP)
