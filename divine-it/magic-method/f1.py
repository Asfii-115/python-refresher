class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __getattr__(self, attr):
        return f"{attr} not found"

    def __setattr__(self, attr, value):
        print(f"Setting {attr} to {value}")
        super().__setattr__(attr, value)


p = Person("Alice", 30)
print(p.name)  # Alice
print(p.height)  # height not found (via __getattr__)
p.age = 31


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"


# Usage
greet = Greeter("Hello")
print(greet("Alice"))  # Hello, Alice! (via __call__)
