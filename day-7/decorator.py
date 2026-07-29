# basic idea 

# def decorate(function):
#   def wrapper(*args, **kwargs):
#     print("i am decorating this function")
#     function(*args, **kwargs)
  
#   return wrapper

# @decorate
# def hello_world(person):
#   print(f"hello {person}")

# hello_world("utkarsh")



# logging 

def logged(function):
  def wrapper(*args, **kwargs):
    value  = function(*args, **kwargs)
    with open('log_file.txt','a+') as f:
      fname = function.__name__
      print(f"{fname} returned value {value}")
      f.write(f"{fname} returned value {value}\n")
    return value 
  
  return wrapper


@logged
def add(x,y):
  return x+y

print(add(10,20))
print(add(10,20))
print(add(10,20))
print(add(10,20))


