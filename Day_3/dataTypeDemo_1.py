
# data type: 
x=1j
print(type(x)) #<class 'complex'>

#Observe carefully.
#1)List-->[]
print("#######Prints List of An Elements :")
x=["Apple","Mango","Guava","Perry"] #list -->[]
print(type(x))  #<class 'list'> ---> for list subscript operator is used --->[]
##################################

#2)tuple--> ()
print("#######prints tuples :")
x=("Laptop","Tablet","Mouse") 
print(type(x))  #<class 'tuple'>
##################################

#3)range--> ()
print("#######prints range from 0 to 10")
z=range(10)
print(type(z)) #range(0, 10)
#convert to list to display the content of x:
print(list(z)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
###################################

#4)Dictionary --->{key:value}
print("prints Dictionary type of data")
y={"Name":"Yogesh","Age":31} #key:vlaue pair-->Dictionary:key value pair-->{}
print(y)
print(type(y))
###################################

#5)string
print("#######prints String type of data :")
x="Yogesh"
print(type(x)) #<class 'str'>
####################################

#6)int
print("#######prints integer type of data :")
x=20
print(type(x)) #<class 'int'>
###################################

#7)float
print("#######prints flaot type of data :")
x=20.5
print(type(x))
###############################

#6)frozenset
print("#######prints frozen type of data :")
x=frozenset(("Apple","Mango","Guava","pomegranate"))
print(x)
print(type(x))
###############################

#7)bool
x= True 
print(x)
 
 # display type ox x
print(type(x))

###############################
#8)bytes
x=b"123"
print(x)

print(type(x))
###############################
#9)bytearray
x = bytearray(5)
print(x)

print(type(x))
###############################
#10)memoryview
x = memoryview(bytes(5))
print(x)

print(type(x))
###############################
#11)NoneType
x=None
print(x)

print(type(x))
#1)int,flaot,complex - Numeric Types
#2)str -text type
#3)Sequence Types- list,tuple,range
#4)Mapping Type- dict
#5)Set Types- set,froenset
#6)Boolean type- bool
#7)Binary Types- bytes,bytearray,memoryview
#8)None Type- NoneType

