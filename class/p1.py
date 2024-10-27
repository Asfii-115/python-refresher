# example 1
class Car:
    def __init__(self, make, year) -> None:
        self.make = make
        self.year = year

    def describe(self):
        print(f"Model is {self.make} and year is {self.year}")


car1 = Car("Toyota", 2020)
# print(car1.make)
# print(car1.year)
# car1.describe()

# example 2 (do a review)
class BankAccount:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdraw):
        self.balance -= withdraw


account = BankAccount("asfi", 500)
account.deposit(200)
account.withdraw(400)
print(account.balance)


class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def add_trick(self, trick):
        li = []
        li.append(trick)
        return li


dog1 = Dog("odo")
dog1.add_trick("roll over")
print(dog1.add_trick)


class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        return (self.length + self.width) * 2


r1 = Rectangle(5, 10)
print(r1.length, r1.width)
r1.area()
r1.perimeter()


class Grade:
    def __init__(self, name, points) -> None:
        self.name = name
        self.points = points

    def add_grade(self):
        li = []
        return li.append(self.points)

    def avg(self):
        return sum(self.points)
