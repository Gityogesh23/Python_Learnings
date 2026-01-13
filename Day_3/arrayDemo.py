# To print an String starts with A
print("Using Startswith()")
a = ["Akshay","Bala","akshit","Ananya","Ansh","sharad"];
# check letter
b = 'A';
#using startswith()
res = [ i for i in a if i.lower().startswith(b.lower())]
print(res)

#Using lambda,filter
#Filter() with a lambda makes it easy to filter names by their first letter, 
#ignoring case. It’s a clean, modular approach that works great in functional programming, especially when chaining operations.

print("Using filter Only")
res=list(filter(lambda i: i[0].lower()==b.lower(),a))
print(res)

#using List comprehension:List comprehension provides a quick way to filter names by 
#comparing the first letter of each string after converting it to lowercase. 
#It is particularly effective for simple, case-insensitive checks and works well for 
#small to medium-sized lists.

print("Using List Comprehension")
res = [i for i in a if i[0].lower() == b.lower()]
print(res)