
#INHERITANCE:

'''
Accessing members of one class inside another class

1. By Composition (HAS-A Relationship)
2. By Inheritance (IS-A Relationship)



1. By Composition (HAS-A Relationship):
By using class name or by creating object we can access members of one class inside another class. It is called as Composition.

Ex: 
class Engine:
    def m1():
        pass
    
    def m2():
        pass

class Car:
    c = Engine
    c.m1()
    c.m2()

#Here, HAS-A relationship is used
#Car has a Engine relationship    

'''


'''
WAPP to achieve HAS-A relationship taking Employee HAS-A Car as relation
'''


print("\t\t\t******Accessing member of one class by another through Composition: Employee HAS-A Car Relationship******")
class Car:
    def __init__(self,c_name,c_cost,c_year):
        self.c_name = c_name
        self.c_cost = c_cost
        self.c_year = c_year

    def cm(self):
        print("\n\tCar Model Name is : ",self.c_name)
        print("\tCar Cost is : ",self.c_cost)
        print("\tCar Model Year is : ",self.c_year)

class Employee:
    def __init__(self,e_name,e_role,cr):
        self.e_name = e_name
        self.e_role = e_role
        self.cr = cr

    def em(self):
        print("\tEmployee Name is : ",self.e_name)
        print("\tEmployee Role is : ",self.e_role)
        Car.cm(cr)

cr = Car("Maruti",500000,2000)

emp = Employee("Ramesh","Software Architect",cr)
emp.em()






'''
Accessing members of one class inside another class

1. By Composition (HAS-A Relationship) #Explained above

2. By Inheritance (IS-A Relationship) #Explained below
#We use the Parent and child class concept

syntax:
class P:
    constructors | methods | variables

class C(P):
    m1()

#Here Class C is Child class. and Class P is parent class.
'''

#WAPP to illustrate the working of Parent and Child class concept [include all types of variables and methods in Parent and access these via child class. Child class should not contain any methods/variables]
print("\n\t\t\t******Accessing members of one class by another: Parent and Child Class (IS-A Relationship)")
class P:
    a = 10 #static variable

    def __init__(self):
        self.b = 20 #instance variable

    @classmethod
    def m1(cls):
        print("Parent Class-Method")

    @staticmethod
    def m2():
        print("Parent class Static-method")

    def m3(self):
        print("Parent class Instanc-method")



class C(P):
    pass

c1 = C()
print(c1.a)
print(c1.b)
c1.m1()
c1.m2()
c1.m3()


'''
Guess whether the following python code will get executed or not. And mention reasons for throwing errors
'''

class Parenttest:
    a=10

    def __init__(self):
        self.b=20


class Childtest(Parenttest):
    c = 30

    def __init__(self):
        self.d = 40

c1 = Childtest()
#print(c1.a, c1.b, c1.c, c1.d)
#AttributeError: 'Childtest' object has no attribute 'b'
#Here, we get this AttributeError because if a child class has constructor , then we will be not be abe to access parent class constructor. In order to access parent class constructor, use super().__init__() in the child class constructor




'''
WAPP to access parent class constructor by child class
'''

class Parenttest1:
    a=10

    def __init__(self):
        self.b = 20

class Childtest1(Parenttest1):
    c = 30

    def __init__(self):
        super().__init__()
        self.d = 40

c2 = Childtest1()
print(c2.a, c2.b, c2.c, c2.d)




#In the above previous code, we just accessed the constructor of parent class. Now, we will see how to pass parameters from child class and get initialization done by parent class using super().__init__(p1,p2)
print("\n\t\t\t******passing parameters to Parent class using super().__init__(p1,p2) to get the initalization task done by parent class******")
class Person:
    def __init__(self,e_name,e_age):
        self.e_name = e_name
        self.e_age = e_age

    def eat_drink(self):
        print("\nEat and Drink...")

class Employee(Person):
    def __init__(self,e_name,e_sal,e_id,e_age):
        super().__init__(e_name,e_age)
        self.e_id = e_id
        self.e_sal = e_sal

    def work(self):
        print("\nEmployee is into coding...")

    def empinfo(self):
        print("\tEmployee Name is:",self.e_name)
        print("\tEmployee salary is:",self.e_sal)
        print("\tEmployee id is:",self.e_id)


e1 = Employee("Ramesh", 120000, 12891,32)

e1.eat_drink()
e1.empinfo()
e1.work()



# IS-A vs HAS-A:
'''
#When to use IS-A relation?
#If we want to extend the functionalities of an existing class , we prefer IS-A relationship 
#Ex 1: Relation between Employee and Person is a type of IS-A relationship.  For the existing class Person, we can extend it for adding new functionalities of Employee.
#Ex 2: Relation between Tablets and Medicine is a type of IS-A relationship.  For the existing class Medicine, we can extend it for adding new functionalities of Tablets.

#When to use HAS-A relation?
#If we do not want to add new functionalities and extend but only want to utilize existing class functionalities , then at that time, we prefer HAS-A relationship
#Ex 1: Relation between Employee and a Car HAS-A relationship. wherein, Employee class cannot extend Car class for adding any new functionalities but Employee class can make use of existing Car class.  
#Ex 2: Relation between Person and a Home HAS-A relationship. wherein, a Person class cannot extend Home class for adding any new functionalities but Person class can make use of existing Home class.
'''


#WAPP in combination of both IS-A and HAS-A relationship
print("\n\t\t\t******Combination of IS-A and HAS_A relationship in python")
class Car:
    def __init__(self,c_name,c_cost,c_year):
        self.c_name = c_name
        self.c_cost = c_cost
        self.c_year = c_year

    def car_details(self):
        print("\tCar Model is:",self.c_name)
        print("\tCar Price is:",self.c_cost)
        print("\tCar Model Year is:",self.c_year)

class Person:
    def __init__(self,emp_name,emp_age):
        self.emp_name = emp_name
        self.emp_age = emp_age

    def task(self):
        print("Person is Sleeping")

class Employee(Person):
    def __init__(self,emp_name,emp_age,emp_salary,emp_id,c1):
        super().__init__(emp_name,emp_age)
        self.emp_salary = emp_salary
        self.emp_id = emp_id
        self.c1 = c1

    def empinfo(self):
        print("Employee Name is :", self.emp_name)
        print("Employee Age is :", self.emp_age)
        print("Employee ID is :", self.emp_id)
        print("Employee Salary is :", self.emp_salary)
        self.c1.car_details()
        

c1 = Car("Mahindra", 4500000, 2023)
emp = Employee("Suresh",38,120000,123128,c1)
emp.empinfo()
emp.task()





#COMPOSITION VS AGGREGATION:
'''
Consider two HAS-A relationships:
i).  University HAS-A Department
ii). Department HAS-A Professor


i).  University HAS-A Department:
Here, University is a container Object. And Department is a contained object.

In real world scenario, Without the existence of a University(container object),  department(contained Object) cannot exist. 
Now, Without the existing of container object, if contained objects cannot exist, then such a relation is called as "Composition"

#Objects are strongly associated in Composition. Ex: Inner classes


ii). Department HAS-A Professor
Here, Department is a container Object. And Professor is a contained object. Suppose, If a Department is closed due to shortage of students, the professors can be moved to another department. So, without the existence of Department, there is a still chance of existence of professor.

In real world scenario, Without the existence of a Department (container object), there is still a chance of existence of Professors (contained object). Such a relation is called as "Aggregation"

#Objects are weakly associated in Aggregation.
'''



#Example:

class Student:
    college_name = "NIT"
    def __init__(self,name):
        self.name = name
#Here, relation between Instance-variable and class is composition. (i.e, Without Student there is no chance of existence of student_name)
#Here, relation between class and static-variable is aggregation.(i.e, Without existence of Student_name, there is a chance of existence of College Name)
