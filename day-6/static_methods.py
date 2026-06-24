"""
static method-> a method that belongs to a class rather than any object from that class-> good for utillity function

instance method -> best for operation on instance of a class( object )

"""

class Employee:
  count =10

  def __init__(self, name, pos):
    self.name = name
    self.pos =pos

  def get_info(self):
    return f"{self.name} == {self.pos}"
  
  @staticmethod
  def is_Valid(position):
    valid_pos = ["hr", "pd", "dev"]
    print(count)
    return position in valid_pos
  
e1 = Employee("utk", "hr")
e2= Employee("rahul","cook")

print(e1.get_info())
print(Employee.is_Valid("dev1"))
print(Employee.is_Valid("dev"))