
# you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Tuples are defined by enclosing comma-separated elements within parentheses ().
x = ("apple", "banana", "cherry")
y = list(x)
print(x) ;
y[1] = "kiwi"
x = tuple(y)

print(x)