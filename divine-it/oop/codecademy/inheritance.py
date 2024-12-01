class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id+=1

    def say_id(self):
        print(f'My id is {self.id}')

class Admin(Employee):
    pass  

e3 = Admin()
e3.say_id()