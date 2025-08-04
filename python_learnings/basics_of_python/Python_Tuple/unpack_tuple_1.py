# Python - Unpack Tuples -->Unpacking a Tuple
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to
# collect the remaining values as a list.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
