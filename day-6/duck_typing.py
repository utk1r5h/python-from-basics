"""
duck typing - another way apart from inheritance, 
              objects must have the min necessary attributes and methods
"""


class Animal:
  alive = True

class Dog(Animal):
  def speak(self):
    print("woof")


class Cat(Animal):
  def speak(self):
    print("meow")

class Car:
  alive = False
  def speak(self):
    print("honking")


animals = [Dog(), Cat(), Car()]

for animal in animals:
  animal.speak()
  print(animal.alive)