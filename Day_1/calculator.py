num1= int(input("Enter the first number--> "))
num2= int(input("Enter the Second number-->"))
print("numbers are-->",num1,num2)

choice=(input("Options : +,-*,/,%  :" ))

if(choice == "+"):
    addition_of_two_num = num1 + num2
    print("Addition :",addition_of_two_num)

elif(choice == "-"):
    sub_of_two_num = num1 - num2
    print("Subtraction :",sub_of_two_num)

elif(choice == "*"):
    product_of_two_num = num1 * num2
    print("Product :",product_of_two_num)
    
elif(choice == "/"):
    division_of_two_num = num1 / num2
    print("Division :",division_of_two_num)

elif(choice == "%"):
    Remainder_of_two_num = num1 % num2
    print("Product :",remainder_of_two_num)
else:
    print("invlid choice")