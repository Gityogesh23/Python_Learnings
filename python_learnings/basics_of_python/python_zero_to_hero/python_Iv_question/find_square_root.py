import math

list_of_numbers=(4,9,36,64,81,144,121,324); #list of numbers

# Calculate square root of numbers and store in a list

square_root=[math.sqrt(num) for num in list_of_numbers];
print(square_root);


"""
1. math.sqrt(num)
math.sqrt() is a function from Python’s math module.

It takes a number (num) and returns its square root.

Example:

python
Copy
Edit
math.sqrt(81)  # returns 9.0
2. for num in list_of_numbers
This is a loop that goes through each element in list_of_numbers one by one.

On the first pass, num is 4 → then 9 → then 36 → … until the last number.

3. [ ... for num in list_of_numbers ]
The square brackets mean:
“Collect the results into a new list.”

On each loop, the result of math.sqrt(num) is added to this list.

4. Whole process step-by-step:
If list_of_numbers = (4, 9, 36):

Loop starts: num = 4 → math.sqrt(4) = 2.0 → put in list

Next: num = 9 → math.sqrt(9) = 3.0 → put in list

Next: num = 36 → math.sqrt(36) = 6.0 → put in list

Result:

python
Copy
Edit
square_root = [2.0, 3.0, 6.0]

"""
