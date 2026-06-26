
name = input("please enter your name: ")

with open("names.txt", "a") as file:

  file.write(f"{name}\n")


#file.close()-> instead of close more pythonic way is to use-> with

with open("names.txt", "r") as file2:
  lines = file2.readlines()

for line in lines:
  print(f"hello, {line}", end ="")



with open("names.txt", "r") as file2:
    for line in file2:
      print(f"hello, {line}", end="")




names = []

with open("names.txt") as file2:
  for line in file2:
    names.append(line.rstrip())


for name in sorted(names):
  print(f"hello {name}")