"""
composition- the composed object directly owns its component, which can not exist independently 
              "owns a" relationship
               
              
"""


class Engine:
  def __init__(self, hp):
    self.hp = hp

class Wheel:
  def __init__(self,size):
    self.size = size 

class Car:
  def __init__(self, make, model, h_p, size_wheel):
    self.make = make
    self.model = model
    self.engine = Engine(h_p)
    self.wheel = [Wheel(size_wheel) for wheel in range(4)]
  
  def disp(self):
    return f"{self.make}, {self.model}, {self.engine.hp}, {self.wheel[0].size}"

car = Car("bmw", "sedan", 100, 18)

print(car.disp())