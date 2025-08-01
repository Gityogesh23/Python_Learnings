# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary,
# all with different qualities and usage.
#
# A tuple is a collection which is ordered and unchangeable.


# Tuples are defined by enclosing comma-separated elements within parentheses ().
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# All Duplicates
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Tuple Length
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# Create Tuple With One Item
# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# Tuple Items - Data Types
# tuple1 = ("apple", "banana", "cherry")
# print(tuple1)
# tuple2 = (1, 5, 7, 9, 3)
# print(tuple2)
# tuple3 = (True, False, False)
# print(tuple3)
#
# # A tuple can contain different data types:
# # A tuple with strings, integers and boolean values:
#
# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

## Access Tuples in Python -->in python negave indexing also works
# consider above example
# print(thistuple[-2]);
# print(thistuple[0]);
# print(thistuple[-1]);


 #print tuples by giving an range -->#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[3:5])
# giving only first 5th items names excluding 5th -->i.e melon
print(thistuple[:5])

# By leaving out the end value, the range will go on to the end of the tuple: giving all from "cherry" till end..
print(thistuple[2:])