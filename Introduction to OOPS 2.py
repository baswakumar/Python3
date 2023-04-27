#We can create 'n' number of objects for a single class
#Below example demonstrates it.
l1=[1,2,3,4,5]
l2=['a',4,'o',9]
l3=[350]

print(type(l1))
#list is an object which belongs to in-built class "List"

#NOTE: class Name should always start with Upper-case. However, pre-defined class can start wit lower-case.
#NOTE: variable name can use camel-case

#NOTE: The constructor has always first argument as 'self'.
#Ex: def __init__(self,)

#During initialization of constructor, default value concept is not applicable in python

#When is a constructor called ?
#When an object is created, the corresponding constructor is called.
#The constructor is not called explicitly
#Below program demonstrates it.

class Exam:
    def __init__(self):
        print("This is called from constructor, automatically")
t=Exam()

#What should be te name of constructor?
# __init__

#What is the purpose of Constructor?
#1. To declare declare and initialize object variables.

#How many times a Constructor will be executed?
#Only once per object
#Below code demonstrates it
class Home:
    def __init__(self):
        print("Constructor called only once per object")
#Here, t1, t2, t3 and t4 are object reference variables and not object.
# NOTE: The constructor is executed only once per object i.e, Home() 
t1=Home()
t2=Home()
t3=Home()
t4=Home()

#Constructor should take atleast 1 argument and i.e, self
#Error name: __init__() takes 0 positional arguments but 1 was given
#Below program demonstrates that we get an error if we do not pass atleast 1 argument in constructor
#To execute this below code, uncomment the documentation comment by removing the ''' and then run it
'''
class Rent:
    def __init__():
        pass

r = Rent()
'''

#Is Constructor Mandatory?
#No, in case constructor is not declared, the python will implicitly provide a constructor
#Below code demonstrates on whether constructor is mandatory or not

class Chair:
    pass

c = Chair()
#Here, the above code, we have not declared any constructor. But, implicitly python provides a constructor

#Is Constructor overloading allowed in Python?
#Yes, it is but the last constructor gets the priority over others.

#How does the Constructor Overloading work in Python?
#Suppose, assume we have 4 constructors in a class. 
#The order of declaration of constructor plays an important role.
#The last declared constructor takes priority over others.

#Below Python code will demonstrate how the last constructor takes priority over other constructor
'''
class Continent:
    def __init__(self):
        print("No Arg constructor from Continent class")
        
    def __init__(self,x):
        print("No Arg constructor from Continent class")

    def __init__(self,x,y):
        print("No Arg constructor from Continent class")


c1=Continent()
'''
#The above code will not get executed and throws error
#Error Name: TypeError: Continent.__init__() missing 2 required positional arguments: 'x' and 'y'
#The error is because, as per python the last constructor takes priority over other constructors        
#Since, last constructor accepts 2 arguments, but none are passed during object creation.


#To understand this concept, another slightly tweaked python code below can help understand better
class Ocean:
    def __init__(self):
        print("No arg constructor from Ocean class")

    def __init__(self,x,y):
        print("Two args constructor from Ocean class")

    def __init__(self,x):
        print("One arg constructor from Ocean class")

oc=Ocean(120)
#The above code will get executed as expected because:
#The last constructor takes priority over other constructors in python and,
#Also the last constructor expects 1 argument and same one argument is passed during object creation

    


