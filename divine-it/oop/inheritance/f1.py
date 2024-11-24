class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f'id of {self.name} is {self.id}')

class Employee(Person):
    def print(self):
        print('employee class called')


em = Employee('kai',19) 
em.display()
em.print()                   