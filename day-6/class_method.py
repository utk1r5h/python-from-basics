"""
allow operation related to class itself, take cls as argument 


static method: best for utility func that do not need access to class data 
class method: best for class level data or require access to the class itself


"""

class Student:
  count =0
  total_cg =0
  def __init__(self, name, cg):
    self.name = name 
    self.cg = cg
    Student.count +=1
    Student.total_cg+=cg
  
  def get_info(self):
    return f"{self.name} == {self.gpa}"
  
  @classmethod
  def get_count(cls):
    return f"Total number of student: {cls.count}"
  
  @classmethod
  def avg_gpa(cls):
    if cls.count==0:
      return 0
    return f"avg gpa is: {cls.total_cg/cls.count}"


s1 = Student("utkarsh", 8)
s2 = Student("nishu", 8.5)
print(Student.get_count())

print(Student.avg_gpa())