class Student:
  class_year = 2028
  num_students =0
  def __init__(self, name, age):
    self.name = name 
    self.age = age 
    Student.num_students+=1


student1 = Student("abc", "18")
student2 = Student("def", "20")


print(student1.name, student1.age)
print(student1.class_year, student2.class_year)
print(Student.class_year)

print(Student.num_students)

student3= Student("ghi", 19)
print(Student.num_students)



