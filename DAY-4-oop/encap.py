class Model:
  def __init__(self, model_type):
    self.model_type=model_type
    self._weights = None
    self.__secret_key = "123"


m = Model("linear regression")
print(m.model_type)
print(m._weights)
print(m._Model__secret_key)


# name mangling prevents inheritance protection


# instance variable -> any variable stored inside the object 
# class variable -> any object stored inside the class 



"""
Class variables live in the class.

Instance variables live in the object.

Reading:
Object -> Class -> Parent Classes

Writing:
obj.x = ...
always writes to the object.

"""

class Person:
  def __init__(self, age):
    self._age = age
  def get_age(self):
    return self._age
  def set_age(self, value):
    if value<0:
      raise ValueError("age cant be negative")
    self._age = value

p = Person(20)
print(p.get_age())
print(p.set_age(50))
print(p.get_age())


