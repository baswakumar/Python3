#Introduction to OOPS
#Class is  blueprint that contains variables (instance, static and local variables) and methods (instance, static and class methods)

#A brief about types of variables
#Instance -> Object level variables
#Static -> Class level variables 
#Local -> method level variables

#How to define a class
class class_name:
    pass

#What is documentation string?
#It is an optional used to add details for the code and acts as a multi-line comment in the long run.
#documentation string is a class-level method.

#Example of documentation string
class docString:
    '''This is a sample documentation string with details
    @author: Baswa Kuar
    @Year: 2023
    @Language: Python
    @Version:3'''



#How to access the documentation string details?
#There are 2 ways to access the documentation string
#1. By using the print(ClassName.__doc__)
class docString:
    '''This is a sample documentation string with details
    @author: Baswa Kuar
    @Year: 2023
    @Language: Python
    @Version:3'''
    print(docString.__doc__)

#2.By using the help from terminal. (Go to terminal)

help(docString)
class docString:
    '''This is a sample documentation string with details
    @author: Baswa Kuar
    @Year: 2023
    @Language: Python
    @Version:3'''
    help(docString)


#constructor starts with: __init__
#constructor in python is also called as magic method

#sample code for constructor
class SampleConstructor:
    '''This python code contains basic constructor'''
    def __init__(self):
        self.name="Baswa"
        self.marks=100
        self.height=5.2

    def details():
        print("My name is",self.name)
        print("My marks are",self.marks)
        print("My height is",self.height)

#Function vs method in python.
'''
If it is declared outside the class, it is called as function.
If it is declared inside the class, then it is called as method.
'''

#Function example
def f1():
    #This is a python function
    pass


#Method example
class Customclass:
    def m1():
        #This is a python method
        pass



#Object Creation:
class SampleConstructor:
    '''This python code contains basic constructor'''
    def __init__(self):
        self.name="Baswa"
        self.marks=100
        self.height=5.2

    def details(self):
        print("My name is",self.name)
        print("My marks are",self.marks)
        print("My height is",self.height)

s = SampleConstructor()
# Here, s is a reference variable of object
# Here, SampleConstructor() is an object

#How to access the variables & methods inside a class?
#Using object reference, we can access the variables & methods inside a class as shown below

print(s.name)
print(s.height)
print(s.marks)
s.details()

#What is self?
#It is current object reference variable
#It is a python provided implicit variable pointing to current object
#By using self, we can access object related variables(instance variables) and object related methods (instance methods)
#Since, self is not a keyword/reserved word, We can use any alternative name, 
#But, as a good programming practice, compulsorily use "self" while making references

#Write a python program to define Employee class and create an object for that class
class Employee:
    def __init__(self,ename,eno,eid,eage):
        self.ename=ename
        self.eno=eno
        self.eid=eid
        self.eage=eage
    
    def describe(self):
        print("Hello, My name is:",self.ename )
        print("My Employee Number is", self.eno)
        print("My Employee ID is:",self.eid)
        print("My age is:",self.eage)

e=Employee("Baswa",12345,"E12121",100)
e.describe()

#Can I create two or more objects & object reference variables for a single class?
#Yes, continuing the above code, I can create multiple objects & object reference variables as shared below

e1=Employee("Kumar",54321,"K32323",99)
e1.describe()

# e and e1 are two different objects stored at two differnet memory locations
print(id(e))
print(id(e1))

#Instance variables name are important not the passing variables name.
#Example consider the same above snippet of code with small variation, where passing parameters are x,y and z (does not play a key role while accesing) but instance variables are cname, model_year and price (play a vital role while accessing)

class Car:
    def __init__(self, x, y, z):
        self.cname = x
        self.model_year=y
        self.price=z
    
    def car_details(self):
        print("Car Name is:",self.cname)
        print("Car Model Year is:",self.model_year)
        print("Car Price is",self.price)

c = Car("Mercedez Benz",2024,1234567.89)
c.car_details()

