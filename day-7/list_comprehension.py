# 1

values = []

for x in range(10):
  values.append(x)




values = [x+1 for x in range(10,20)]
print(values)

# The original list is replaced, not extended.


#2 

even = []

for x in range(51):
  if x%2==0:
    even.append(x)




even = [x for x in range(50,101) if x%2==0]
print(even)



#3



options = ["any", "albany", "apple", "world", "hello", ""]

valid_strings =[string for string in options if len(string)>=2 if string[0]=='a' if string[-1]=='y']

print(valid_strings)


#4 


matrix =[[1,2,3],[4,5,6]]
flat =[]

flat = [num for row in matrix for num in row ]
print(flat)




#5 if else block 


category = [ "even" if x%2==0 else "odd" for x in range(10)]
print(category)


# 6 nested list 
