# class Employee:
#     id=10
#     name="Devansh"
#     def display(self):
#         print(self.id,self.name)
# b=Employee()
# b.display()
# a = Employee()
# del a.id
# a.display()




# class car:
#     def __init__(self,modelname, year):
#         self.modelname = modelname
#         self.year = year
#     def display(self):
#         print(self.modelname,self.year)
# c1 = car("Toyota", 2016)
# c1.display()



# class car:
#     def __init__(self):
#         print("ghjk")
#     def display(self,modelname,year):
#         print(modelname,year)
# c1 = car()
# c1.display("Toyota", 2016)


# class Student: 
#     def __init__(self): 
#         print("The First Constructor") 
#     def __init__(self): 
#         print("The second constructor") 
 
# st = Student() 
# -------------------------------------------------------------------------------------
# BUILT-IN CLASS FUNCTIONS
# class Student:
#  def __init__(self,name,id,age):
#         self.name = name
#         self.id = id 
#         self.age = age
    
# s = Student("John", 101, 22)
# print(getattr(s,'name'))
# setattr(s,"age",23)
# print(getattr(s,'age'))
# print(hasattr(s,'id'))
# delattr(s,'age')
# print(s.age)
# --------------------------------------------------------------------------
# INHERITANCE
# 1.SINGLE INHERITANCE
# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# class Dog(Animal):
#     def bark(self):
#         print("dog barking")

# d=Dog()
# d.bark()
# d.speak()
# ---------------------------------------------------------------------------------
# COPYING-SHALLOW COPY AND DEEP COPY
# import copy
# original_list = [1, 2, [3, 4]]
# shallow_copied_list = copy.copy(original_list)
# shallow_copied_list[2][0] = 99
# print(original_list)

# import copy
# original_list = [1, 2, [3, 4]]
# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[2][0] = 99
# print(original_list)
# print(deep_copied_list)
# --------------------------------------------------------------------
# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         # print("ID: %d \nName: %s"%(self.id,self.name))
#         print(f"ID : {self.id} Name : { self.name}")

# emp=Employee()
# emp.display()
# ----------------------------------------------------------------------------------
# Create a Person class with attributes name and age. 
# Then, create an Employee class that inherits from Person and adds employee_id.
# Override the __init__ method in Employee using super()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Employee(Person):
#     def __init__(self, name, age, employee_id):
        
#         super().__init__(name, age)
#         self.employee_id = employee_id

# emp = Employee("Aisha", 28, "EMP1023")
# print(emp.name)        
# print(emp.age)         
# print(emp.employee_id) 
# --------------------------------------------------------------------------------
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number  
#         self.__balance = balance                


#     def get_balance(self):
#         return self.__balance

   
#     def set_balance(self, amount):
#         if amount < 0:
#             print("Balance cannot be negative.")
#         else:
#             self.__balance = amount

# account = BankAccount("ACC1001", 5000)
# print(account.get_balance())  
# account.set_balance(7000)
# print(account.get_balance())  
# account.set_balance(-100)   
# ------------------------------------------------------------------------------
# Create an abstract class Vehicle with abstract methods start() and stop(). Implement: Subclasses Car and Bike with specific implementations.
# from abc import ABC, abstractmethod
# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def start(self):
#         print("Car engine starts with a key or button.")

#     def stop(self):
#         print("Car engine stops.")


# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a kick or self-start.")

#     def stop(self):
#         print("Bike engine stops.")


# car = Car()
# bike = Bike()

# car.start()
# car.stop()

# bike.start()
# bike.stop()
# --------------------------------------------------------------------------------------------
# Implement method overriding by creating a Shape class and subclasses Circle and Square.
# class Shape:
#     def area(self):
#         print("Calculating area of a shape")


# class Circle(Shape):
#     def area(self, radius):
#         return 3.14 * radius * radius


# class Square(Shape):
#     def area(self, side):
#         return side * side

# circle = Circle()
# square = Square()

# print("Circle Area:", circle.area(5))
# print("Square Area:", square.area(4))
# -------------------------------------------------------------------------------
# class Matrix:
#     def __init__(self, data):
#         self.data = data

#     def __mul__(self, other):
#         result = [[sum(self.data[i][k] * other.data[k][j]
#         for k in range(len(other.data)))
#             for j in range(len(other.data[0]))]
#                 for i in range(len(self.data))]
#         return Matrix(result)

#     def __str__(self):
#         return "\n".join(str(row) for row in self.data)
# m1 = Matrix([[1, 2],[3, 4]])

# m2 = Matrix([[5, 6],[7, 8]])

# print(m1 * m2)
# ----------------------------------------------------------------------
# class Book:
#     count = 0 
#     def __init__(self, title): 
#         self.title = title 
#         Book.count += 1     
#     @classmethod 
#     def total_books(cls): 
#         return f"Total books created: {cls.count}" 
    
# book1 = Book("Python Basics") 
# book2 = Book("Advanced Python") 
# print(Book.total_books()) 
# ----------------------------------------------------------------------
