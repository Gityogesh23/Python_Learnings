
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
print("Find by Name of Emplyee from Employees List:")


