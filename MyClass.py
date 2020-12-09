### Python class
"""
As soon as you define a class, a new class object is created with the same name. 
This class object allows us to access the different attributes as well as to instantiate 
new objects of that class.
"""

class MyClass:
  "This is my class"
  a = 10
  def func(self):
    print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function myclass.func at 0x7f04d158b8b0>
print(MyClass.func)

# Output: 'This is my class'
print(MyClass.__doc__)

"""
You may have noticed the self parameter in function definition inside the class but, 
we called the method simply as ob.func() without any arguments. It still worked.

This is because, whenever an object calls its method, the object itself is passed as 
the first argument. So, ob.func() translates into MyClass.func(ob).
"""


### Python constructor
"""
In Python, a method with name __init()__ is a constructor. 
This method is automatically called when an object is instantiated.
"""
class ComplexNumber:
    def __init__(self,r = 0,i = 0):  # constructor
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))


c1 = ComplexNumber(2,3) # Create a new ComplexNumber object
c1.getData() # Output: 2+3j

c2 = ComplexNumber() # Create a new ComplexNumber object
c2.getData() # Output: 0+0j


### Python Inheritance
class Mammal:
    def displayMammalFeatures(self):
        print('Mammal is a warm-blooded animal.')

class Dog(Mammal):
    def displayDogFeatures(self):
        print('Dog has 4 legs.')

d = Dog()
d.displayDogFeatures()
d.displayMammalFeatures()

#To learn more : https://www.programiz.com/python-programming/inheritance