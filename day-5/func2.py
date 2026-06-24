class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True
  
  def eat(self):
    print(f"{self.name} is eating")
  
  def sleep(self):
    print(f"{self.name} is sleeping")


class Dog(Animal):
  def speak(self):
    print("hi")
  

class Cat(Animal):
  def speak(self):
    print("hello")
  

class Mouse(Animal):
  def speak(self):
    print("hey")


dog = Dog("abc")
cat = Cat("def")
mouse = Mouse("ghi")

print(dog.name, cat.name, mouse.name)
dog.speak(), cat.speak(), mouse.speak()