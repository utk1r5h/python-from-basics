"""
dunder methods
automatically called by many of python's built in operations 
allow to define and customize behavior of objects 

__str__ -> return string representation of an object

__eq__

__lt__


__getitem__


"""

class Book:
  def __init__(self, title, author, num_pages):
    self.title =title
    self.author=author
    self.num_pages=num_pages
  
  def __str__(self):

    return f"{self.title} by {self.author}"
  
  def __eq__(self, other):
    return self.title ==other.title and self.author == other.author
  
  def __add__(self, other):
    return self.num_pages + other.num_pages
  
  def __contains__(self, item):
    return item in self.title or item in self.author
  
 

B1 =Book("hobbit", "tolkien", 300)
B2 = Book("Harry potter", "jk rowlng", 500)
B3 = Book("abc", "def", 100)
B4 =  Book("abc", "def", 1100)

print(B1)
print(B3==B4)

print(B1+B2)

print("Harry" in B2)

print(B1.title)
