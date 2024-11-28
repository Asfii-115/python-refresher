class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} years old'

    def __repr__(self):
        return f'{self.name}, {self.age} years old'

p = Person('alice',30)
print(p)
print(repr(p))       
        