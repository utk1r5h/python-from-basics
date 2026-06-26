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




import csv

# students = []

# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for row in reader: 
#     students.append({"name": row[0], "home": row[1]})




# # def get_name(student):
# #   return student["house"]

# # for student in sorted(students, key = get_name):
# #   print(f"{student['name']} lives in {student['house']}")



# for student in sorted(students, key = lambda student: student["name"]):
#   print(f"{student['name']} lives in {student['home']}")




# students = []

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader: 
#     students.append({"name": row["name"], "home": row["home"]})




# # def get_name(student):
# #   return student["house"]

# # for student in sorted(students, key = get_name):
# #   print(f"{student['name']} lives in {student['house']}")



# for student in sorted(students, key = lambda student: student["name"]):
#   print(f"{student['name']} lives in {student['home']}")



# name = input("whats your name? ")
# home = input("where do u live? ")

# with open("students.csv", "a") as file:
#   writer = csv.writer(file)
#   writer.writerow([name, home])


name = input("whats your name? ")
home = input("where do u live? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"name": name, "home": home})



