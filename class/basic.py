# creating class
class MyClass:
    x = 5


# creating object
o1 = MyClass()
print(o1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.name})"

    def my_func(self):
        print("Hello, My name is " + self.name)


p1 = Person("Asfi", 24)
p1.name = "peco"
del p1.age
print(p1)
p1.my_func()
