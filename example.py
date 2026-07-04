################ *for ##############
list1=["RBR","SS","YM"]
for x in list1:
    print(x)
############### *Range ################
n=90
for i in range(1,n,3):
    print(i)


############### *patten ##############
n=5
for i in range(0,n):
    print(i*"*")

############## *args##################
def Cars(*cars):
    print(cars)
    print(cars[1])
    print(cars[2])
    print(cars[:2])
Cars("Tata indica","OOOO","BMW")

################# *kwargs #######################

def Cars_and_Owners(**cars):
    print(cars["Tataindica"],cars["OOOO"],cars["Benz"])

Cars_and_Owners(Tataindica ="Rohanth",OOOO="Sowmiya",Benz="Yuva")

##################### _iter_ ##################

class Cars2:
    cars=[]
    def __init__(self,cars):
        self.cars=cars
    
    def __iter__(self):
        return iter(self.cars)

c1 = Cars2(["Tata indica","OOOO","BMW"])
for x in c1:
    print(x)

###########__next__############ 

a = ['a', 'e', 'i', 'o', 'u']

iter_a = iter(a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))###copy###

############# built-in imports #########

from math import sqrt, pi

print(sqrt(400))

################split & Strip ##############
rbr = " kdjf sldkfbv dkbl kibvl adibdb "
print(list(rbr.strip(" ")))
print(list(rbr.split(" ")))
print(list(rbr.strip().split(" ")))

################# custom modules ############ 
from cus_module import sample
sample("hi")

################ Datetime #################
import datetime
appointment = datetime.datetime(2026, 7, 25, 14, 30)
message = appointment.strftime("Your appointment is on %A, %B %d at %I:%M %p.")
print(message)

############## math & random ##############
import math
import random
print(math.sqrt(16))   
print(math.ceil(4.2))     
print(math.floor(4.8))  
print(math.pow(2, 3))     
print(math.pi)           
print(math.log(100, 10))  
print(random.random())        
print(random.randint(1, 10))  
print(random.uniform(1.5, 5.5)) 
print(random.choice(['apple', 'banana', 'cherry'])) 
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)  

################ JSON ################
#https://www.geeksforgeeks.org/python/serialize-and-deserialize-complex-json-in-python/


############### string formatting ###################
name = "Yuva"
age = 21
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

############### Exception Handling ###############
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

#raise
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
print(withdraw(5000, 2000))

################ OOPs ####################
#https://www.geeksforgeeks.org/python/python-oops-concepts/
#task1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}")
    def get_statement(self):
        print("Owner:", self.owner)
        print("Current Balance: ₹", self.balance)
account = BankAccount("Yuva")
account.deposit(5000)
account.withdraw(2000)
account.withdraw(4000)
account.get_statement()
#Task2
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} the Dog barks: {self.sound}")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} the Cat meows: {self.sound}")
animal = Animal("Cow", "Moo")
dog = Dog("Bruno", "Woof")
cat = Cat("Kitty", "Meow")
animal.speak()
dog.speak()
cat.speak()
#Task3
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self, subject, score):
        self.grades[subject] = score
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    def report(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:")
        for subject, score in self.grades.items():
            print(subject, ":", score)
        print("Average:", self.get_average())
student = Student("Yuva", "IT101")
student.add_grade("Python", 90)
student.add_grade("Java", 85)
student.add_grade("DBMS", 95)
student.report()




