#task 1  :string concatenation
from operator import truediv

first_name = "John"
last_name = "Doe"
print(first_name+" "+last_name)
str=" ".join([first_name,last_name])
print(str)

#Task 2: length of string
str2="Hello World"
print(len(str2))

#Task 3: Sub string using slicing
str3="Python Programming"
print(str3[-11:])

#Task 4: upper and lower
str4="Equilar"
print(str4.upper())
print(str4.lower())

#Task 5:Check if a String is a Number
num1="1234"
print(num1.isnumeric())
num2="12a3"
print(num2.isnumeric())

#Task set 2

#task1:Add, Subtract, Multiply, Divide Two Numbers
a=10
b=5
print(a+b)
print(a-b)
print(a/b)

#task2 Check if a Number is Even or Odd
num3=4
if num3%2==0:
    print("even ")
else:
    print("odd")

#task 3 : Calculate the Area of a Circle
radius=5
area=3.14*radius*radius
print(area)

#task 4:Round a Float to 2 Decimal Places
num4=3.14159
format=f"{num4:.2f}"
print(format)

#task 5:Use int(), float(), str() to Convert Types
print(int("123"))
print(float("3.14"))

numb4=45
s=str(numb4)
print(s)

#Task Set 3: Type Casting Practice

#task1: Convert str_num and add
num5 = 5
str_num = "10"
print(int(str_num)+num5)

#task 2:  Input Two Numbers as Strings, Multiply Them as Integers
print(int("4")*int("5"))

#task3 : Convert a Float to an Int and Observe the Change
print(int(9.81))

#task 4:Cast Boolean to Integer and Back
val1=True
val2=False
print(int(val1), int(val2))
