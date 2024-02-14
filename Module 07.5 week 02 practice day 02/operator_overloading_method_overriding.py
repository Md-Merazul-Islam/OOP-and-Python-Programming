# # #operator overloading
"""Operator overloading is the ability to redefine the behavior of operators beynod their perdefined meaning. For example, the (+) operator can be use no only for adding numbers buts also for conectenating string and merging list."""

class vector :
    def __init__(self,a) -> None:
        self.a =a
    def __add__(self,other):
        return self.a + other.a
    def __mod__(self,other):
        return self.a % other.a

a1= vector(1)
a2= vector(3)
print(a1+a2)
print(a1%a2)



#method overriding:
"""
Method overriding is a concept in inheritance where a subclass provides a specific implementation of a method that is already defined in its superclass. This allows a subclass to provide a specialized implementation of a method that is already defined in its parent class.
"""

class Animal:

    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def speak(self):
        print("Dog Speak")
        
    
a1= Animal()
a1.speak()

dog= Dog()
dog.speak
    
    