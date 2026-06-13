# for loop

for i in range(5):
  print(i)

# range type -> (start, end, step)

for i in range(10,1,-1):
  print(i)

print("\n new \n")

for i in range(1,10,2):
  print(i)


arr = [10,20,30,"utkarsh"]

for i in arr:
  print(i)


#enumerate gives both index and value

for index, value in enumerate(arr):
  print(index, value)

for index, ch in enumerate("utkarsh"):
  print(index, ch)



# prob 1 -> print sqaured 

for i in range(1,11,1):
  print(i*i)


# prob 2 -> count vowels in a string
ans =0

for ch in "utkarsh":
  if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    ans=ans+1

print(ans)  

for ch in "utkarsh":
  if ch in "aeiou":
    ans = ans+1

print(ans)


# prob 3-> reverse a string using a loop

rev=""

for ch in "utkarsh shukla":
  rev = ch + rev

print(rev)


# 2d loops 

for i in range(3):
  for j in range(4):
    print("*", end="")
  print()


for i in range(10):
  for j in range(i):
    print("*",end="")
  print()


# diamond pattern 

n=4 

for i in range(1, n+1):
  print(" "*(n-i), end="")
  print("*"*(2*i-1))

for i in range(n-1,0,-1):
  print(" "*(n-i), end="")
  print("*"*(2*i-1))