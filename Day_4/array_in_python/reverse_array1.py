# t]To reverse an list inside Array

a= ["Pritam","Priya","Nidhi","Akshada","Ananya","Arav","Anant","Ajit"]
print("Print Array Elements are :")

'''for i in a:
    print(i)
    o/p:on newline so refer best and simple next method for onle line o/p
'''
print(a) #TO print one single line
print("Print array elements in reverse order")
a= (a[::-1])  # Creates NEW reversed list O(n)
print(a) 

# Best way in O(1)
print("new list of nummbers/numeric values:")
a1=[12,13,14,190,200,300] #[] means list its mutable[add,remove,change ]:append(),reverse() and pop() but 
#(1,2,3,4,)-->tuple object immutable ops:count(),index() only
print("reversed new list:")
a1.reverse()
print(a1) 
'''
Original:  [12, 14, 15, 18, 19, 200]
Indices:    0   1   2   3   4    5
Negative:  -6  -5  -4  -3  -2   -1

[::-1] extracts:
1st: index -1 → 200
2nd: index -2 → 19  
3rd: index -3 → 18
4th: index -4 → 15
5th: index -5 → 14
6th: index -6 → 12

'''
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

"""
a = [12, 14, 15, 18, 19, 200]     # List ✅ Can modify
a[0] = 99                          # Works: [99, 14, 15, 18, 19, 200]
a.append(300)                      # Works: [99, 14, 15, 18, 19, 200, 300]

b = (12, 14, 15, 18, 19, 200)      # Tuple ❌ Cannot modify
b[0] = 99                          # ERROR: 'tuple' object does not support item assignment

"""

