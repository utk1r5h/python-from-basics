# multiple C(A,B)
# multi lever C<-B<-A

class Animal:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print(f"{self.name} animal is eating")
  
  def sleep(self):
    print(f"{self.name} animal is sleeping")


class Prey(Animal):
  def flee(self):
    print(f"{self.name} animal is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} animal is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass


r1= Rabbit("rabbi")
h1 = Hawk("hawki")
f1= Fish("fishi")

r1.flee()
f1.flee()
f1.sleep()
f1.hunt()