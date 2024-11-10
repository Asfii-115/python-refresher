# class Employee:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

# e1 = Employee(111,'john',20) 
# print(e1)       
# print(e1.__str__())       
# print(e1.__repr__()) 
# print(str(e1))      
class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def __str__(self):
        return f'Employee id is {self.id} and name is {self.name} and age is {self.age}' 

    def __repr__(self):
        return f'Employee id is {self.id} and name is {self.name} and age is {self.age}' 

e1 = Employee(111,'john',20) 
print(e1)       
print(e1.__str__())       
print(e1.__repr__()) 
print(str(e1))      