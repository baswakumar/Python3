#GARBAGE COLLECTION

#When to use a garbage collection?
#If an object does not contain any reference variable, at that time it is eligible for  GC
print("\n\t\t\t****** GARBAGE COLLECTION******")
import gc
print("By default GC value is: ",gc.isenabled())
gc.disable()
print("After disabling GC value is: ",gc.isenabled())
gc.enable()
print("After enabling GC value is: ",gc.isenabled())


#Destructors:

#Who calls the Destructors?
#Garbage Collector

#When does the Garbage collector calls the destructor?
#Just before destroying the object 

#For what purpose the Garbage Collector calls destructor?
#To perform clean-up activities

#Is the job of Destructor is to destroy object?
#No, the job of destructor is just to perform clean-up activity.
#Garbage collector is responsible for destroying object

#Syntax of destructor
def __del__(self):
    pass


'''
WAPP to demonstrate the working of Garbage collector
'''
print("\n\t\t\t******Single object and Garbage Collection process******")
import time
class GC:
    def __init__(self):
        print("\n1.Object Initialization")
        
    def __del__(self):
        print("\n2.Actions performed and ready for clean-up activity...")


gc = GC()
print("\n3.Using gc for requirement")
time.sleep(5)
print("\n4.Work with gc is completed and making it ready for Garbage collection process")
gc = None
time.sleep(5)
print("\n5.Termination")





'''
WAPP to demonstrate the working of 1 object and multiple object references working with Grbage collection  
'''
print("\n\t\t\t****** Multiple Object References and Garbage Collection process ******")
class GCC:
    def __init__(self):
        print("\nObject Initialized")

    
    def __del__(self):
        print("\nAction is performed successfully and object is now ready for cleanup activity ...")


gcc = GCC()
gcc1 =gcc
gcc2 =gcc1

del gcc
time.sleep(5)
print("\nObject not yet destroyed after deleting gcc")

del gcc1
time.sleep(5)
print("\nObject not yet destroyed after deleting gcc1")

del gcc2
time.sleep(5)
print("\nThis time the object will be destroyed")
print("\nEnd of application")
#NOTE: Until and unless the last reference is deleted, the object will not get destroyed



'''
What is difference between "del t1" and "t1 = None"

Similaarity is: Both are now eligible for Garbage collection

Differences are:
#del t1
#In this case, object will be destroyed and variable t1 is also destroyed. if you try to print(t1), it will throw error: NameError

#t1=None
#In this case, variable is there but corresponding object will be destroyed. Later, t1 can be used for other purposes
'''

#WAPP to demonstrate the working of lists and Garbage collection
print("\n\t\t\t****** List and Garbage Collection process ******")
class GCL:
    def __init__(self):
        print("\nObject is initialized")

    def __del__(self):
        print("\nDestroyed object")


l = [GCL(),GCL(),GCL()]
del l
time.sleep(5)
print("\nEnd of application")





#WAPP to demonstrate the working of lists and Garbage collection (Automatic process)
print("\n\t\t\t****** List and Garbage Collection process (Automatic) ******")
class GCLA:
    def __init__(self):
        print("\nObject is getting initialized...")

    def __del__(self):
        print("\nDestroyed object ...")


la = [GCLA(),GCLA(),GCLA()]
time.sleep(5)
print("\nEnd of application")
#NOTE: Even though, no explicitly 'del' or assigning to None value is done here, the garbage collector is called automatically at the end of program


#How to get the reference variables count?
# using sys.getrefcount(object_name)
# 
# WAPP to count the number of reference variables

print("\n\t\t\t****** Counting References for an object ******")
import sys
class R:
    def __init__(self) -> None:
        pass
r1 = R()
r2 = r1
r3 = r2
r4 = r3

del r2, r3, r4
print(sys.getrefcount(r1))
#Output: 2 . Although there is just one reference, there is another reference called 'self'




















