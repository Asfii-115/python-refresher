class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def speak(self):
        return self.bark()


my_dog = Dog("budy", 5)
print(my_dog.name, my_dog.age)
print(my_dog.bark())


class Puppy(Dog):
    def __init__(self, name, age, is_playful=True) -> None:
        super().__init__(name, age)
        self.is_playful = is_playful

    def play(self):
        return (
            f"{self.name} is playing!"
            if self.is_playful
            else f"{self.name} is too tired to play."
        )

    def speak(self):
        return f"{self.name} say squeak!"


my_puppy = Puppy("Max", 1)
print(my_puppy.bark())  # Inherited from Dog class
print(my_puppy.play())  # Unique to Puppy class
print(my_puppy.is_playful)  # Output should be True

print(my_dog.speak())  # Output should be "Buddy says Woof!"
print(my_puppy.speak())
