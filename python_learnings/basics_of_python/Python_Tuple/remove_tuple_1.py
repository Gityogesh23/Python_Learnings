# Remove Items
# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

thistuple=("cherry","mango","pomegranate","pineapple");
y=list(thistuple);
y.remove("pineapple");
print(y);

# Or you can delete the tuple completely:

# same code as above just change
# thistuple = ("apple", "banana", "cherry");
# del thistuple;
#
# print(thistuple) ;#this will raise an error because the tuple no longer exists