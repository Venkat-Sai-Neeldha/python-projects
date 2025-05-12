#1#1. Match Statement – Day of the Week
day=int(input("enter  day number:  "))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day")

#2. For Loop – Multiplication Table

number=int(input("enter  number:  "))
for i in range(1,11):
    print(f"{number} X {i}={number*i}")

#3 While Loop – Number Guessing Game
import random
num=-1
attempts=0
generatedno=random.randint(1, 100)
while num!=generatedno:
    num=int(input("enter your number:  "))
    attempts+=1
    if num<generatedno:
        print("too low")
    elif num>generatedno:
        print("too high")
    else:
        print(f"Correct! you have gussed it in {attempts} attempts")

#4 function -prime number checker
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True

for i in range(1,100):
    if is_prime(i):
        print(i)

#5. Lambda – Sorting a List of Tuples
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

sortedlist = sorted(people, key=lambda person: person[1])

print(sortedlist)

#6. Arrays – Reverse an Array
list1=[1,5,3,4,2]
print(sorted(list1,reverse=True))

#7)7. Class and Object – Bank Account

class BankAccount:
    def __init__(self):
        self.balance = 0
    def withdraw(self, amount):
        self.balance -= amount
        return f"withdrew {self.balance}"
    def deposit(self, amount):
        self.balance += amount
        return f"deposited {self.balance}"
    def current_balance(self):
        return f"current_balance {self.balance}"

account=BankAccount()
print(account.current_balance())
print(account.deposit(1000))
print(account.withdraw(500))
print(account.current_balance())

#88. For Loop – Fibonacci Series
num=int(input("Enter a number: "))
a=-1
b=1
for i in range(num):
    c=a+b
    print(c)
    a,b=b,c

#9 factorial of a given number
n=int(input("Enter a number: "))
if n < 0:
    print("Factorial not defined for negative numbers")
else:
    result = 1
    while n > 1:
        result =result*n
        n -= 1
    print("Factorial is:", result)

#10 10. Function – Palindrome Checker
def is_palindrome(word):
    if word == word[::-1]:
        return "is palindrome"
    else:
        return "is not palindrome"

print(is_palindrome("radar"))

