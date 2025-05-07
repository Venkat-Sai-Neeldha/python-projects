
#1) Area of rectangle
length=5
breadth=4
area=length*breadth
print(area)

# user input:avg of 3 numbers
a,b,c=map(int,input().split())
print("enter a b c values with single spaces")
average=(a+b+c)/3
print(average)


#2)Compare two numbers and print which one is greater, or if they are equal.
a=10
b=20
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print("both are equal")

#Check if a person is eligible to vote (age ≥ 18).
age=int(input())
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#3)Check if a number is within the range (10, 50)
num=int(input())
if num>=10 and num<=50:
    print("with in the range")
else:
    print("not in the range")

#validate user login and password using logical and
username="venkat"
password="abcd1234"

print("enter username and password")
input_user=input("enter username: ")
input_password=input("enter password: ")
if input_user==username and input_password==password:
    print("login successful")
else:
    print("login failed")


#4) assignment operators
variable=20
variable+=5
print(variable)

variable-=5
print(variable)

variable*=2
print(variable)

variable/=2
print(variable)

#Bitwise operators

val1=5
val2=3
print(val1 & val2)
print(val1 | val2)
print(val1 ^ val2)