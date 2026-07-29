import numpy as np

from numpy.lib.stride_tricks import sliding_window_view

mat = np.arange(16).reshape(4,4)

windows = sliding_window_view(mat, (2,2))


kernel = np.array([[1,0], [0,-1]])


print(windows)
print(((kernel*windows).sum(axis=(2,3))))








# inheritance 
# encapsulation. Encapsulation means hiding internal data and controlling access through methods.

# he fundamental programming concept of bundling data (variables) and the methods (functions) that operate on that data into a single unit (typically a class). It restricts direct access to internal components, protecting data from unauthorized modification and ensuring it is only accessed through defined, controlled methods




#Polymorphism in Object-Oriented Programming (OOP) allows different objects to respond to the same method name in their own unique way. Derived from the Greek words for "many forms", it lets you write generic code that can process distinct data types through a unified interface

"""
It does not ask

Is this object a Duck?

Instead it asks

Can this object do quack()?

Python focuses on behavior, not type.



Duck typing is a Python concept where an object's suitability is determined by the methods or behavior it supports rather than its actual class or inheritance hierarchy


Polymorphism means the same interface produces different behaviors.
"""







"""
 property is a special type of class attribute that executes custom logic (methods) whenever it is accessed, modified, or deleted, while maintaining the clean syntax of a standard data attribute.
"""


"""
Structural OverviewConceptWhat it isHow it works in PythonPolymorphismThe overall goal."I want a single function to process different types of objects."Duck TypingThe mechanism."I will look for the method name at runtime, completely ignoring the object's class ancestry."
"""




"""
 abstraction - the process of hiding complex internal implementation details and showing only the essential features to the user
"""