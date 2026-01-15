# t]To reverse an list inside Array

a= ["Pritam","Priya","Nidhi","Akshada","Ananya","Arav","Anant","Ajit"]
print("Print Array Elements are :")

'''for i in a:
    print(i)
    o/p:on newline so refer best and simple next method for onle line o/p
'''
print(a) #TO print one single line
print("Print array elements in reverse order")
a= (a[::-1])
print(a)

#TO print elemetns before index 3
# In python :-indicates start 
print("prints elements before index 2")
 #prints elements before index 2
number_list = [2,4,6,8,10,12]

print(number_list[2:])
# [6, 8, 10, 12]

print("prints elements after index 2")
number_list = [2,4,6,8,10,12]

print(number_list[:2])
# [6, 8, 10, 12]

#collection[start:stop:step] Use with collections-List,Array,String
'''
The step parameter works in an interesting way. This is used to specify the sequence 
to be followed while slicing through a collection.
::2-->
We used a step value of 2. This means the list will jump two steps repeatedly during 
the iteration
The first element is 2. Two steps from 2 lands us at 6. Two steps from 6 lands us at 10. 
Two steps from lands us nowhere because there is no other element to complete the second step.
'''
number_list = [2,4,6,8,10,12]

print(number_list[::2]) # [2, 6, 10]
print(number_list[::3]) # [2,8,]