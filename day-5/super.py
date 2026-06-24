class Shape:
  def __init__(self, color, filled):
    self.color = color
    self.filled = filled 
  
  def dsc(self):
    print(f"it is {self.color} and it is {self.filled}")

 

class Circle(Shape):
  def __init__(self, color, filled, radius):
    super().__init__(color,filled)
    self.radius = radius
  
  def dsc(self):
    print(f"it is a circle with the area of {3.14*self.radius*self.radius}cm^2")
    super().dsc()

class Square(Shape):
  def __init__(self, color, filled, width):
    super().__init__(color, filled)
    self.width = width

class Traingle(Shape):
  def __init__(self, color, filled, width, height):
    super().__init__(self, color, filled)
    self.width = width
    self.height=height 


circle = Circle("red", True, 50)
square = Square("blue", False, 10)
print(circle.radius, circle.color, circle.filled)
print(square.width, square.color, square.filled)


circle.dsc()



# call methods from parent class, extend the functionality of inherited methods 
