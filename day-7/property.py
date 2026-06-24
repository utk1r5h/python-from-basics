"""
@property

method as property
accessed like an attribute
add additional logic when read write or delete attributes

getter, setter and deleter method 


"""


class Rectangle:
  def __init__(self, width, height):
    self._width=width
    self._height=height
  
  @property
  def width(self):
    return f"{self._width:.1f}cm"

  @property
  def height(self):
    return f"{self._height:.1f}cm"
  

  @width.setter
  def width(self, new_width):
    if new_width>0:
      self._width=new_width
    else:
      print("width must be greated than zero")

  @width.deleter
  def width(self):
    del self._width
    print("width deleted")

R1 = Rectangle(10,20)
print(R1.width, R1.height)
R1.width =12
print(R1.width, R1.height)
R1.width =-1

del R1.width