'''
WAPP to demonstrate the passing of members from one class to another
'''

class Employee:
    def __init__(self,ename,esal):
        self.ename = ename
        self.esal = esal

    def display(self):
        print("Employee Name is : ",self.ename)
        print("Employee salary is : ",self.esal)


e1 = Employee("Ramesh",100000)

class Scholars:
    def scholar(self,ex):
        e1.display()

s1 = Scholars()
s1.scholar(e1)


#===========OR=============

class Employees:
    def __init__(self,ename,esal):
        self.ename = ename
        self.esal = esal

    def displays(self):
        print("Employee Name is : ",self.ename)
        print("Employee salary is : ",self.esal)


e1 = Employees("Suresh",200000)

class Scholar:
    def scholars(ex):
        e1.displays() #accessing methods from other class

Scholar.scholars(e1)#Passing members happens here




#INNER CLASS
#A class within another class is called as inner class

#When to use inner classes?
#Without existing one type of object if there is no chance of existing another type os object, then inner classes should be used.



class Home: #Here, class Home is outer class
    class Kitchen: #Here, class Kitchen is inner class
        pass
#Here, in the above snippet, without existence of outer class, there is no chance for existence of inner class

print("\n\t\t\t****** INNER CLASSES CONCEPT******")

class Outer:
    def __init__(self) -> None:
        print("Outer class object creation...")

    class Inner:
        def __init__(self) -> None:
            print("Inner class object creation...")

        def display(self):
            print("Inner class method called...")


o = Outer()
i = o.Inner()
i.display()

#OR (1st way),  
'''
i = Outer().Inner()
i.display()
'''

#OR (2nd way),
'''
Outer().Inner().display()
'''

#NOTE: Any number of inner classes can be created.

'''
class World:
    class Continent:
        class Country:
            class State:


'''

'''
WAPP to demonstrate the inner class concept using 2 inner classes and 1 outer class
'''
print("\n\t\t\t******2 INNER CLASSES AND 1 OUTER CLASS******")
class World:
    def __init__(self):
        print("\nWelcome to the World")
        self.cont = self.Continent()
        self.cont1 = self.cont.con()

        self.cntr = World.Continent.Country()
        self.cntr2 = self.cntr.countries()

        
    class Continent:
        def __init__(self):
            print("\nWelcome to the Continent")
        
        def con(self):
            print("Inner class continent accessed")

        class Country:
            def __init__(self):
                print("\nWelcome to the Country")
            
            def countries(self):
                print("Inner class Country accessed")

w = World()

#NESTED METHODS
#A nested method is a method inside another method 

#What is the purpose of Nested methods?
#To use a method specific repeatedly required functionality.

print("\n\t\t\t******NESTED METHODS******")

class Test:
    def test1(self):
        def calculation(a,b):
            print("\nSum is: ", a+b)
            print("Product is: ",a*b)
            print("Average is: ",(a+b)/2)
        calculation(10,20)
        calculation(100,200)
        calculation(5,10)
        calculation(2,10)

t1 = Test()
t1.test1()




