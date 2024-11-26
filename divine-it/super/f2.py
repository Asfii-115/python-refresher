class Parent:
    def greet(self):
        print('hello from parents')

class Child(Parent):
    def greet(self):
        super().greet()
        print('hello from child')

child = Child() 
child.greet()

#----constructor------
class Parent2:
    def __init__(self, name):
        self.name = name
        print(f'parent name: {self.name}')

class Child2(Parent2):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f'child name: {self.name} and age: {self.age}')    

c = Child2('kai',23)

#----------multiple inheritance---------
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()  # Calls A's greet method

class C(B):
    def greet(self):
        print("Hello from C")
        super().greet()  # Calls B's greet method

# Usage
c1 = C()
c1.greet()

# Output:
# Hello from C
# Hello from B
# Hello from A

        
                