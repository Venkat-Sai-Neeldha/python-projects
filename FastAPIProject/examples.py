# 1. Arithmetic, Comparison & Logical Operators
a = 10
b = 3
print("Addition:", a + b)           # 13
print("Subtraction:", a - b)        # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.333...
print("Floor Division:", a // b)    # 3
print("Exponentiation:", a ** b)    # 1000
print("Modulus:", a % b)            # 1

print("Equal:", a == b)             # False
print("Greater Than:", a > b)       # True
print("Not Equal:", a != b)         # True
print("Less than or equal to:", a <= b)
print("Greater than or equal to:", a >= b)

x = 5
x += 2
print("x after += 2:", x)           # 7
print("Logical AND:", (x > 5) and (x < 10))  # True
print("Logical OR:", (x > 5) or (x < 3))     # True
print("Logical NOT:", not(x == 7))          # False

# 2. Control Flow (if, elif, else, nested if)
x = int(input("Enter a number: "))
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Nested If Example
if x > 0:
    if x > 10:
        print("x is large positive")
    else:
        print("x is small positive")

# 3. Loops: for, while, break, continue
for i in range(3):
    print("For loop:", i)

count = 0
while count < 3:
    print("While loop:", count)
    count += 1

for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print("Control Statement Loop value:", i)

# for-else loop
for i in range(3):
    print("Counting:", i)
else:
    print("Loop completed")

# Reverse loop
for i in range(5, 0, -1):
    print("Reverse:", i)

# 4. Data Structures: List, Tuple, Set, Dictionary

# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "yellow")
print("List:", fruits)  # ['apple', 'yellow', 'banana', 'cherry', 'orange']

# Tuple
coordinates = (10.0, 20.0)
numbers = (5, 10, 15)
print("Tuple item:", coordinates[0])
print("Tuple slice:", numbers[0:2])

# Set
unique_numbers = {1, 2, 3, 3}
print("Unique set:", unique_numbers)

a_set = {1, 2, 3}
b_set = {3, 4, 5}
print("Union:", a_set | b_set)
print("Intersection:", a_set & b_set)

# Dictionary
person = {"name": "Alice", "age": 30}
person["city"] = "New York"
info = {"name": "Bob", "age": 25}
info.update({"job": "Engineer"})
print("Person dict:", person)
print("Updated info dict:", info)

# 5. User Input, Type Conversion, Error Handling
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print(f"Age: {age}, Height: {height}m")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input, please enter a valid integer.")

# 6. Functions
def greet(name):
    print(f"Hello, {name}!")

def add(a, b=5):
    return a + b

def multiply(x, y):
    return x * y

def describe_person(name, age=18):
    return f"{name} is {age} years old."

greet("Venkat")
print("Sum with default:", add(3))         # 8
print("Sum with both args:", add(3, 4))    # 7
print("Product:", multiply(4, 5))          # 20
print(describe_person("Lily"))             # Lily is 18 years old.
print(describe_person("Tom", 22))          # Tom is 22 years old.

