class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Negative age")
        self._age = value

p = Person(20)

print(p.age)

p.age = -10

print(p.age)