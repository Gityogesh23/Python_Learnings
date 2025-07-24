x=5;
y=12;
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b;
print(sum(x,y));  #sum of x,y
print(sub(x,y));  #substraction of x,y
print(mul(x,y));  #mutliplication of x,y
print(div(x,y));  #division of x and y

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x="yogesh";
y="kiran";
print(x);
print(y);

#Casting
# If you want to specify the data type of a variable, this can be done with casting.
x=str(3); # it is '3'
print(x);

y=int(3); # it's 3
print(y);

z=float(3); # it's 3.0
print(z);



# if i want to print types of variables used above i.e x and y
print(type(x));
print(type(y));
print(type(z));
