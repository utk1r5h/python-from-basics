"""
Aggregation= Represents a relationship where one object(the whole)
             contains references to one or more independent objects ( the parts)

"""

class Library:
  def __init__(self, name):
    self.name = name
    self. books = []
  
  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    return [f" {book.title} by {book.author} "for book in self.books ]

class Book:
  def __init__(self, title, author):
    self.title =title
    self.author = author



L1 = Library("new delhi lib")
b1 = Book("HP 1", "JK Rowling")
b2 = Book("hobbit", "tolkien")
b3 = Book("1984", "orwell")


L1.add_book(b1)
L1.add_book(b2)
L1.add_book(b3)

print(L1.name)
print(L1.list_books())