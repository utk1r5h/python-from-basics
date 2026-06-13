i=0

while i<5:
  print(i,end=" ")
  i=i+1

print()


  # use1 -> to iterate user to input something 
check = True

while check:
  s = input("Enter: ")
  if s=="exit":
    check = False


# reverse digit

n = 12345

while n>0:
  digit = n%10
  print(digit,end="")
  n//=10


# / -> this always produces float 
# // -> this gives floor division


# check palindrome number 

n=121 
rev=0
temp=n



while n>0:
  digit = n%10
  rev = rev*10+digit
  n//=10

print(rev==temp)

# u can create inside the loop, but cant use a var before defining it inside the loop


# input validation

n=-1

while n<=0:
  n= int(input("enter a pos number"))

  if n>0:
    break
