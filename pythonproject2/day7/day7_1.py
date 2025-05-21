#1) use usermodule
import usermodule as u
print(u.add(2,3))
print(u.subtraction(2,3))
print(u.multiplication(2,3))
print(u.division(2,3))

#2) Package basics with __init__.py

from geometry import circle, rectangle

print("Circle area:", circle(5))
print("Rectangle area:", rectangle(10, 4))

#4) Module‑level vs function‑level scope
list = [1, 2, 3]

def modify_list():
    list.append(4)
    print("Inside function:", list)

modify_list()
print("Outside function:", list)

c = 0

def increment():
    global c
    c += 1
    print("Inside function:", c)

increment()
print("Outside function:", c)


#5)nonlocal keyword practice

def outerfunc():
    message = "Hello"

    def innerfunc():
        nonlocal message
        print("Before change:", message)
        message = "Hi"
        print("After change:", message)

    innerfunc()
    print("Outside inner function:", message)

outerfunc()

#6)  task 6 folder

#7)