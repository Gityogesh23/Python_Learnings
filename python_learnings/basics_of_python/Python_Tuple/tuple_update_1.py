
# you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Tuples are defined by enclosing comma-separated elements within parentheses ().
# x = ("apple", "banana", "cherry")
# y = list(x)
# print(x) ;
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)

# Add Items to Tuples
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), a
# nd convert it back into a tuple.
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple);

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
# create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

