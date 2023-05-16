'''
Define a class Painting and a constructor to initialize variables followed by a method to display the
values held by variables. Use list to declare the values.
'''

class Paint():
    def __init__(self,pname,prate,ppainter):
        self.pname = pname
        self.prate = prate
        self.ppainter = ppainter

    def p_info(self):
        print("\nPaint Name is:", self.pname)
        print("\nPaint Rate is:", self.prate)
        print("\nPainter Name is:", self.ppainter)

#px = Paint('ABC',12345,'Don')
#px.p_info()
p1=[Paint('Acrylic Painting',10000,'Ram'),
    Paint('Canvas Painting',20000,'Sham'),
    Paint('Water Painting',30000,'Ravi'),
    Paint('Oil Painting',40000,'Ramesh')]

for x in p1:
    x.p_info()

#Constructor vs Method
#1. Constructor name is fixed. Methods can have any user defined names.
#2. For constructor , no need to call explicitly. Methods need to be called explicitly.
#3. Constructor is executed only once. Methods can be executed multiple times.
#4. Constructor is used to initialize instance variables. Methods are used for business logic.


'''
WAPP with no constructor and variables being called exclusively
'''

class Bottle():
    def bott(self):
        print("Bottle Brand:",self.b_name)
        print("Bottle Price:",self.b_price)

b1 = Bottle()
b1.b_name="Bisleri" #this is initial and hence no priority
b1.b_price="85"
b1.b_name="Kinley" #This is last and hence takes priority
b1.bott()


###VARIABLES###

#1. Instance Variables:
#Object level variables
#Values of IV varies from object to object

#Where we can declare Instance Variables? And how can we access it?
##1. Inside Constructor using self variable
##2. Inside Instance method using self variable
##3. Outside of the class by using object reference variable

#How to delete an Instance Variable?
##1. Inside a class using: del self.varname
##2. Outside a class using: del objref.varname


'''
WAPP to demonstrate Instance varible using self
'''
class Pillow():
    def __init__(self):
        self.p1=230
        #Instance variable implicitly called and invoked automatically

    def pill(self):
        self.p2=200
        #A variable declared inside a method using self is also an instance variable(provided it is accessed)

px=Pillow()
print("\n",px.__dict__) #Able to see only 1 Instance Variable since not called pill() method

px1 = Pillow()
px1.pill()
print("\n",px1.__dict__)

px2= Pillow()
px2.c4=230 # Instance variable outside the class access using object reference
print("\n",px2.__dict__)

print(px2.p1) #Accesing the Instance Variable outsied the class using object reference


'''
WAPP to demonstrate the working of deletion of Instance variables
'''
class Jar():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def jrd(self):
        del self.b

j4 = Jar(111,222,333,444)
j4.jrd()
del j4.c

print("\n",j4.__dict__)


#2. Static variables:
#Class level variables
#Only one copy will be created at class level
#Where can we declare a static variable?
##1. Inside a class directly
##2. Inside a constructor by using classname
##3. Inside an instance method by using classname
##4. Inside a class method using cls variable (or) classname
##5. Inside a static method using classname

#How can we access Static variables
##1. Inside a constructor using self or classname
##2. Inside an instance method using self or classname
##3. Inside a class method using cls or classname
##4. Inside a static method: by classname
##5. outside a class : either by object reference or by classname



'''
WAPP to demonstrate the working of Static variables
'''
class Printerclass:
    sv1 = 100
    def __init__(self):
        Printerclass.sv2 = 200
        print("\nAccessing Static variable inside a constructor using self: ",self.sv2)
        print("\nAccessing Static variable inside a constructor using classname: ",Printerclass.sv2)

    def printersv(self):
        Printerclass.sv3 = 300
        print("\nAccessing Static variable inside an instance method using self: ",self.sv3)
        print("\nAccessing Static variable inside an instance method using classname: ",Printerclass.sv3)

    @classmethod #Converts the function into a class method & receives implicit first argument as instance method
    def printsv1(cls):
        Printerclass.sv4 = 400
        cls.sv6=600
        print("\nAccessing Static variable inside a class method using cls: ",cls.sv4)
        print("\nAccessing Static variable inside a class method using classname: ",Printerclass.sv4)

    @staticmethod #Converts the function into a static method & does not receive any implicit first argument
    def printsv2():
        Printerclass.sv7=700
        print("\nAccessing Static variable inside a static method using classname: ",Printerclass.sv7)
    
pc = Printerclass()
pc.printersv()
Printerclass.printsv1()
Printerclass.sv5=500
Printerclass().printsv2()
print("\n",Printerclass.__dict__)
print("\nAccessing Static variable outside a class using classname: ",Printerclass.sv1,Printerclass.sv2,Printerclass.sv3,Printerclass.sv4,Printerclass.sv5,Printerclass.sv6,Printerclass.sv7)
print("\nAccessing Static variable outside a class using object reference: ",pc.sv1,pc.sv2,pc.sv3,pc.sv4,pc.sv5,pc.sv6,pc.sv7)

'''
WAPP to demonstrate the working of instance variable, static variable and local variables
'''
class Journal:
    a = 100
    def __init__(self):
        self.a = 200
        Journal.a = 300
        a = 400
        print("a: ",a) #local variable
        print("self.a : ",self.a) #instance variable
        print("Journal.a : ",Journal.a) #static variable

jx = Journal()

#NOTE: Object reference will call only instance variables [Ex: t= Test(). print(t.a)]
#NOTE: Static variables will be called by class level calls. [Ex: print(Test.a)]


'''Guess the output of the following below python code'''

class Machine:
    m1 = 100
    def __init__(self):
        self.t1 = 200
print("\nclass Machine")    
mx1 = Machine()
mx2 = Machine()
print(mx1.m1,mx1.t1)
print(mx2.m1,mx2.t1)

mx1.m1 = 300
mx1.t1 = 400

print(mx1.m1,mx1.t1)
print(mx2.m1,mx2.t1)

'''Guess the output of the following below python code'''
class Fur:
    a = 100
    def __init__(self):
        self.b=2000
fx1 = Fur()
fx2 = Fur()
Fur.a=300
fx1.b = 4000
print("\nclass Fur")
print(fx1.a,fx1.b)
print(fx2.a,fx2.b)

'''
Guess the ouput of the following below python code
'''
class Train:
    a=10
    def __init__(self):
        self.b=20

t1 = Train()
t2 = Train()
t2.a = 30
t2.b =40
print("\nclass Train")
print(t1.a,t1.b)
print(t2.a,t2.b)


'''
Guess the ouput of the following below python code
'''
class Metro:
    a = 100
    def __init__(self):
        self.b = 200

    @classmethod
    def m1(cls):
        cls.a = 300
        cls.b = 400

mx1 = Metro()
mx2 = Metro()

mx1.m1()

print("\n class Metro")
print(mx1.a,mx1.b)
print(mx2.a,mx2.b)
print(Metro.a,Metro.b)



#3. Local variables:
#Method level variables
#They are intitialized / declared within a function and scope belongs to within the function
#They cannot be accessed from outside the function


'''WAPP to demonstrate the working of local variable'''
def localVar():
    lv1 = "This is a local variable"

localVar()
#print("The local variable cannot be accessed from outside the function",lv1)






