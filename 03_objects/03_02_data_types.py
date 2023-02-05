import numpy
"""
In python there are various data types including:
* Sets
* lists (arrays)
* tuples "two-ples"
* dictionaries
"""
#########
## Sets
#########
"""
Sets are mutable, but not ordered. Do not allow duplicates.
"""
# Create a set as:
my_set = {1, 3, 3}
my_set # Duplicates not allowed
my_songset = {'Like a virgin', 'Hills', 'Anaconda'}
my_songset # Order not respected (it was automatically sorted A-Z)
## Can also make one with the set constructor (more on constructors later)
my_set2 = set(('cherries', 'apples', 'bananas')) # Notice the nested ()
my_set2
###########
## Lists
###########
"""
Lists are useful for storing data in a way similar to an array.
These are mutable (can be changed), ordered, and exchangeable (positions of items can be changed).
They also allow duplicate values.
"""
# Lists are created as:
my_list = [1, 3, 4, 9]
friends = ['John', 'Helena', 'Kim', 'Bill']

# Lists are ordered and mutable (items can be changed)
# You can access elements in a list like:
my_list[1] # Python starts at 0
my_list[1:3] # does not include end index
my_list[0:3]
friends[-2]
# Change items in a list
friends[2] = 'Monica'
friends
# Delete elements in a list
# Get length
len(friends)
friends.remove('Helena')
len(friends)
friends

# Can also create with list()
list((2, 3, 4)) # Notice the nested ()

##########
## Tuples
##########
"""
Tuples also allow you to store multiple items into a single variable.
They are like lists (ordered, allows duplicates), but the values & order are unchangeable.
These are useful for things like coordinates where (x, y, z) should not be interchanged in order.
"""
# Creating a tuple
location_tuple = (-33, 12, 4)
tuple_2 = (22, 41, 41, 41, 809)
origin = (0, 0, 0)

#################
## Dictionaries
#################
"""
Contains a list of tuples.
This allows for fast indexing and accessing of values.
Consists of 'key', 'value' pairs where the value can either be a list, string, int, etc.
Can access value with key.
Very useful for storing different data types and is a fast operation
"""
# Create a dictionary as:
recipe_dict = {
    1 : 'Apple Pie',
    2 : 'Pumpkin Pie',
    3 : 'Pecan Pie'
}

recipe_dict
# Get keys
recipe_dict.keys()
# Access value from key
recipe_dict[1]
# Change value for a key
recipe_dict[3] = 'Blueberry Pie'
recipe_dict
# Add to dictionary
recipe_dict[4] = 'Cream Pie'
recipe_dict
# Remove from dictionary
recipe_dict.pop(3)
recipe_dict

# Store in lists
employees = ['John', 'Jessica', 'Monica', 'Kim', 'Layla']
ages = [34, 35, 48, 28, 80]
cities = ['San Diego', 'Boston', 'California', 'California', 'Oregon']

emp_data = {
    'name' : employees,
    'age'  : ages,
    'city' : cities
}
emp_data

emp_data['name']
numpy.mean(emp_data['age'])

# Can also create with dict()
my_team = dict([(33,'john'), (42,'brian'), (89,'earl')]) # Notice use of [] to surround tuples
