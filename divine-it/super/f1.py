class Parent:
    def greet(self):
        print("Hello from the parent")


class Child(Parent):
    def greet(self):
        super().greet()  # greet from parent class
        print("hello from child")


c = Child()
c.greet()


class Animal:
    def __init__(self, species) -> None:
        self.species = species


class Dog(Animal):
    def __init__(self, species, breed) -> None:
        super().__init__(species)
        self.breed = breed


d = Dog("Mammal", "Golden Retriever")
print(d.species)
print(d.breed)
