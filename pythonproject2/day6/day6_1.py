#1) Employee Hierarchy
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def bonus(self):
        return self.salary*0.05

class Hr(Employee):
    def bonus(self):
        return self.salary*0.10

class SeniorEngineer(Employee):
    def bonus(self):
        return self.salary*0.05

class Associate(Employee):
    def bonus(self):
        return self.salary*0.15

emplyees=[Hr("sagar",35000),SeniorEngineer("dhanush",40000),Associate("venkat",25000)]
for e in emplyees:
     print(e.name,"==>",e.bonus())

#2. Vehicle Fleet

class Vehicle:
    def __init__(self,name):
        self.name=name

    def speed(self):
        return 0

    def disp(self):
        print(self.name,"has a speed of",self.speed())

class Car(Vehicle):
    def speed(self):
        return 120

class Bike(Vehicle):
    def speed(self):
        return 60

class Auto(Vehicle):
    def speed(self):
        return 50

vehicles=[Car("thar"),Bike("R15"),Auto("auto")]
for v in vehicles:
    v.disp()

#3)Shape Area Calculator
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
   def __init__(self,width,height):
       self.width = width
       self.height = height
   def area(self):
       return f"area of rectangle is: {self.width * self.height}"



class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return f" area of circle  is: {3.14*self.radius*self.radius}"

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return f" area of triangle is: {0.5*self.base*self.height}"

shapes=[Circle(5),Triangle(5,4),Rectangle(5,6)]
for shape in shapes:
    print(shape.area())

#4)Notification System
class Notification:
    def send_notification(self):
        print("Notification sent successfully")

class PushNotification(Notification):
    def send_notification(self):
        print("push_Notification sent successfully")
class EmailNotification(Notification):
    def send_notification(self):
        print("Email_Notification sent successfully")
class SmsNotification(Notification):
    def send_notification(self):
        print("sms_Notification sent successfully")

def function(Notifications):
    for n in Notifications:
        n.send_notification()
Notifications=[PushNotification(),EmailNotification(),SmsNotification()]
function(Notifications)

#5)Payment Gateway
class PaymentMethod:
    def pay(self,amount):
        return "payment method is {} ".format(amount)

class Paypal(PaymentMethod):
    def pay(self,amount):
        return "paypal amount is {}".format(amount)

class Creditcard(PaymentMethod):
    def pay(self,amount):
        return "credit card amount is {}".format(amount)
class Crypto(PaymentMethod):
    def pay(self,amount):
        return "crypto amount is {}".format(amount)

def checkout(payment_method,amount):
    print(payment_method.pay(amount))
payments = [
    (Paypal(), 100.50),
    (Creditcard(), 250.75),
    (Crypto(), 3000)
]
for payment, amount in payments:
    checkout(payment, amount)






