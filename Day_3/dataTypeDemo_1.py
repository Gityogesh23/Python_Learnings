
# data type: 
x=1j
print(type(x)) #<class 'complex'>

#Observe carefully.
#1)List-->[]
x=["Apple","Mango","Guava","Perry"] #list -->[]
print(type(x))  #<class 'list'> ---> for list subscript operator is used --->[]

#2)tuple--> ()
x=("Laptop","Tablet","Mouse") 
print(type(x))  #<class 'tuple'>
##################################
#3)range--> ()
z=range(10)
print(type(z)) #range(0, 10)
#convert to list to display the content of x:
print(list(x)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
###################################
#4)Dictionary --->{key:value}
y={"Name":"Yogesh","Age":31} #key:vlaue pair-->Dictionary:key value pair-->{}
print(y)
print(type(y))
###################################
#5)string
x="Yogesh"
print(type(x)) #<class 'str'>
###################################
#6)int
x=20
print(type(x)) #<class 'int'>
###################################

#7)float
x=20.5
print(type(x))
###############################

#6)frozenset

###############################
#7)bool

###############################
#8)bytes

###############################
#9)bytearray

###############################
#10)memoryview

###############################
#11)NoneType





#1)int,flaot,complex - Numeric Types
#2)str -text type
#3)Sequence Types- list,tuple,range
#4)Mapping Type- dict
#5)Set Types- set,froenset
#6)Boolean type- bool
#7)Binary Types- bytes,bytearray,memoryview
#8)None Type- NoneType

