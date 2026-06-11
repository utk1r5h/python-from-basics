# dynamically typed --> we dont declare type of variables beforehand

x=10
y="utkarsh"
z=20.5

print(type(x))
print(type(y))
print(type(z))


# numeric -> int, float, complex

a = 3 + 4.5j
print(type(a))
print(a.real)
print(a.imag)


# type conversion

x = 10
print(float(x))
print(complex(x))

y = "100"

#print(int(y))
print(float(y))

x1=10.5 
print(int(x))


s1 = """
this is
the way to create 
multi line string
"""

print(s1)
print(s1[0], s1[10], s1[7])
print(s1[-2]) 

print("hi" *3)


s= "python"
print(s.upper())
print(s.capitalize())

s1="i like this"
print(s1.replace("this", "that"))
print(s1.split())
print(s1.splitlines())


print(s1.find("ke"))


#lists

# ordered, mutable 

nums=[10,200,30,40]


print(nums[0])
nums[1]=100
print(nums[1])

print(nums.append(500))
print(nums.insert(1,200))
print(nums)

print(nums.remove(30))
print(nums)

print(nums.__sizeof__())

print(print(nums[1:4]))
print(len(nums))
nums.sort()

# print(nums)
# a = ["a", "b", "c", "utkarsh"]
# print(len(a))
# a[1]=100
# print(a)


# tuple-> ordered but immputable
t = (10,20,30)
#cant change the elemeents inside the tuple 

new_set = {1,1,2,3,4,4}
print(new_set)

new_set.add(100)
print(new_set)


# dict -> stores key, value pairs

mydetail ={
  "name": "utkarsh",
  "degree": "btech",
  "age":21
}


print(mydetail["degree"])
mydetail["city"] ="delhi"

print(mydetail)


for key, value in mydetail.items():
  print(key, value)


# none is used as a placeholder until a vlaue is assigned to some variable 
