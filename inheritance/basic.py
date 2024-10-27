class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


person1 = Person("John", "Smith")
person1.print_name()


class Student(Person):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.grad_year = year


person2 = Student("Asfi", "x", 2024)
person2.print_name()
print(person2.grad_year)


# def init():
#     parent.init(self, fname, lanme)
