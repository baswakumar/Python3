# TYPES OF METHODS
#1. Instance methods
#2. Class methods
#3. Static methods



#1. Instance methods
#How to access Instance methods outside a class?
#Using the object reference

#How to access Instance methods inside a class?
#Using self reference

class Territory:
    def __init__(self,name, area):
        self.name = name
        self.area = area

    def t_name(self): #This is an instance method
        print("Territory Name is : ",self.name)

    def t_area(self): #This is an instance method
        print("Territory Area is : ",self.area)
        

t1 = Territory("North", 12000)
t2 = Territory("South", 34000)

t1.t_name()
t1.t_area()
t2.t_name()
t2.t_area()
#NOTE: Here, t1.t_name() and t1.t_area() object reference calls are separately called.
#In Below Python code, we will see how an instance method can be called via self reference inside a class 


class KGF:
    def __init__(self, name , price):
        self.name = name
        self.price = price
        #self.k_name #This will not call instance method and hence we need to call self.k_name()
        #self.k_price #This will not call instance method and hence we need to call self.k_price ()
        self.k_name()
        self.k_price()


    def k_name(self):
        print("Gold name is: ", self.name)

    def k_price(self):
        print("Gold price is: ", self.price)

k1 = KGF("Dynamo",145000)

#Getter(accessor) vs Setter(mutator) methods in Python

class Getset:
    def set_name(self,name=''):
        self.name=name
        print("\nSetter Method is called here",self.name)

    def get_name(self):
        print("Getter method is called here")
        return self.name
print("\n ***Examples of Getter& Setter***")    
gx1 = Getset()
gx1.set_name('Ramesh')
print(gx1.get_name())


'''
WAPP to demonstrate getter and setter methods taking "Student Name" and "Student Marks". 
'''

class Student:
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

l = []
print("\n***class Student getter and setter methods***")
s1 = Student()
nos = int(input("Enter number of students: \t"))
#print("Type of nos: ",type(nos))

for i in range (nos):
    names = input("Enter Student Name: \t")
    s1.set_name(names)
    marks = float(input("Enter Marks: \t"))
    s1.set_marks(marks)
    l.append(s1)
    #print(l)

for x1 in l:
    print("")
    print("Student name is: ", x1.get_name())
    print("Student Marks are: ", x1.get_marks())
    
#2. Class Methods
'''
If, there is atleast 1 instance variable, then use instance method.
Else, use class method.

@classmethod
Use this syntax on top of the method to make it a class-method

We can call class-methods using class name or object reference.

'''

#WAPP to demonstrate the working of class method

class Vehicle:
    tires = 4

    @classmethod
    def drive(cls,name):
        print("{} drives with {} Tires".format(name,cls.tires))
print("\n *** Vehicle class Example for Class method ***")
Vehicle.drive('Car')
Vehicle.drive('Jeep')

'''
WAPP to count the number of objects created and display the output in class-method
'''

class Obj:
    Total_count = 0 #Static Variable
    def __init__(self):
        Obj.Total_count= Obj.Total_count + 1

    @classmethod
    def countObjects(cls,Total_count):
        print("Total Number of objects are:",Obj.Total_count) #Accessing only static variable and no instance variable and hence method is made as Class method using @classmethod

tz1 = Obj()
tz2 = Obj()
tz3 = Obj()
tz4 = Obj()
print("Count of objects after creating 4 objects: ",Obj.Total_count)
tz5 = Obj()
tz6 = Obj()
tz7 = Obj()
tz8 = Obj()
print("Count of objects after creating 8 objects: ",Obj.Total_count)




#3.Static method:
###NOTE: If you are using static variables, then use class methods.

#When to use static method?
#Inside a method, if we are not using instance variables and static variables.

#Static methods are general utility methods

#Use @staticmethod to declare explicitly a static method

#Access: Either by class name or by object reference variable

'''
WAPP to demonstrate the working of static method
'''

class ArithmeticClass:
    @staticmethod #Without @staticmethod, it will throw an error:  TypeError: ArithmeticClass.add() takes 2 positional arguments but 3 were given
    def add(x,y):
        print("The sum is: ",x+y)

    @staticmethod
    def product(x,y):
        print("The product is: ", x*y)

    @staticmethod
    def average(x,y):
        print("The average is :",(x+y)/2)

#a1 = ArithmeticClass()
#Here, no need to create instance, because there is no instance method.  
ArithmeticClass.add(10,20)
ArithmeticClass.product(10,30)
ArithmeticClass.average(10,40)
#Here, we are directly accesing the static methods



'''
When to use the static-method, class-method, instance-method ?
1. If Instance Variable only present, then use "Instance-method"
#Explanation 1: If atleast, one instance variable is there, then use instance-method. 
#Because instance variable is key deciding factor 

2. If Static variable only present, then use "class-method"
#Explanation 2: If atlest 1 static variable is there, then use class-method only, 
#Because static variable is key deciding factor

3. If local variable only present, then use "static-method" 
#Explanation 3: They are general utility variables and hence static method

4. If instance variable & static variable are present, then use "instance-method"
#Explanation 4: Here, in this case instance variable is more dominant over static variable and hence it is required to use instance method 
#Because, if atleast 1 instance variable is there, then we need to use instance-method only.

5. If instance variable & local variable are present, then use "instance-method"
#Explanation 5: Here, in this case instance variable is more dominant over static variable and hence it is required to use instance method 
#Because, if atleast 1 instance variable is there, then we need to use instance-method only.

6. If static variable & local variable are present, then use "class-method"
#Explanation 6: Here, in this case of static variable and local variable
#Because, if atleast 1 static variable is there, then we need to use class-method only.
'''
              
        














