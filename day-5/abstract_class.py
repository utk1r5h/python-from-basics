from abc import ABC, abstractmethod

class Vehicle(ABC):
  @classmethod
  @abstractmethod
  def go(self):
    pass


  @classmethod
  @abstractmethod
  def stop(self):
    pass



class Car(Vehicle):
  def go(self):
    print("drive the car")
  def stop(self):
    print("stop the car")


class Bike(Vehicle):
  def go(self):
    print("ride the bike")
  def stop(self):
    print("stop the bike") 

c1 = Car()
c1.go()
c1.stop()


m1 = Bike()
m1.go()
m1.stop()