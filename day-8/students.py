# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     print(f"{name} lives in {house}")


# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append(f"{name} is in {house}")


# for student in sorted(students):
#   print(student)


students = []

with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {}
    student["name"] = name
    student["house"] = house
    students.append(student)


def get_name(student):
  return student["house"]

for student in sorted(students, key = get_name):
  print(f"{student['name']} lives in {student['house']}")

