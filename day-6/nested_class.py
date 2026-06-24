"""
class defined inside another class 

    class outer:
      class inner:

"""
class Profit:
  class Employee:
    def __init__(self, name, position):
      self.name = name
      self.position =position
    def get_details(self):
      return f"{self.name}, {self.position}"

    
  
  def __init__(self, company_name):
    self.company_name=company_name
    self.employees =[]

  def add_emp(self, name, pos):
    new_employee = self.Employee(name, pos)
    self.employees.append(new_employee)
   
  def list_emp(self):
    return [employee.get_details() for employee in self.employees]



C1 = Profit("apple") 
print(C1.company_name)

C1.add_emp("utkarsh", "dev")
C1.add_emp("nishu", "dev-2")
C1.add_emp("abc", "cook")

print(C1.list_emp())

