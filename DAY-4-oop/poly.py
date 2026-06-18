
# method overriding 
# class dog:
#   def speak(self):
#     print("woof")

# class cat:
#   def speak(self):
#     print("meow")


# a = dog()
# b = cat()

# a.speak()
# b.speak()



class duck:
  def quack(self):
    print("quack")

class person:
  def quack(self):
    print("fake duck")

def func(obj):
  obj.quack()

a = duck()
b= person()

func(a)
func(b)
 
# pyhton would only check if the object can respond to quack()
# if the object can perform the required behaviour 



