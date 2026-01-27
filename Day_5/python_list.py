
tuple=(12,13,14,124,"yogesh")
print(type(tuple))  #<class 'tuple'>
print()
print(tuple)

#print(tuple() vs List[])
print("tuple :")
tuple =(12,13,14,15,16,20)
print("type of class :",type(tuple),"or",type(tuple).__name__)

print("List:")
employees=["Yogesh","Kiran","Jayashree","Karishma","Yaksh","Yakshit"]
print("List Of Employees Becomes : ",employees)

#reversed List of employees and tuple thenafter
print("Reversed List Of Employees Becomes: ")
print(employees[::-1]) #step operator ::
print("First in the List Of Employees: ")
print(employees[:1])
print("Fetch Last in the List Of Employees: ")
print(employees[-1])
print("Fetch Employee by Letter: ","Y :")
for emp in employees:
    if emp.lower().startswith("y"):
        print(emp)
#Lists have built-in methods like append(), remove(), pop(), sort(), and len() for length.
#Add Biil Gates at end :append(x)
employees.append("Bill Gates")
print(employees) #o/p:['Yogesh', 'Kiran', 'Jayashree', 'Karishma', 'Yaksh', 'Yakshit', 'Bill Gates']

#pop(index):removes or returns itemat index.
employees.pop(4) #Yaksh will be popfrom list of employees
print(employees) #o/p: ['Yogesh', 'Kiran', 'Jayashree', 'Karishma', 'Yakshit', 'Bill Gates']

#Sort() :sorts in place. i want to sort Jayashree,Kiran,Yogesh,Karishma,Vipul

employees.sort()
print(employees) #o/P:['Bill Gates', 'Jayashree', 'Karishma', 'Kiran', 'Yakshit', 'Yogesh']

#Reverse Order:Add reverse=True for descending sort.
employees.sort(reverse=True) 
print(employees) #O/P:['Yogesh', 'Yakshit', 'Kiran', 'Karishma', 'Jayashree', 'Bill Gates']

#Sort by small letter String first
mixed=["Apple","apple","Mango","mango"]
mixed.sort(key=str.lower)
print(mixed) #['Apple', 'apple', 'Mango', 'mango']

'''
Sort by Length
Use key=len to sort shortest to longest.
'''
words = ["python", "list", "programming"]
words.sort(key=len)
print(words)            # ['list', 'python', 'programming']
