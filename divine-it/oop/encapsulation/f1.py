#-------public------
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age #by default public

    def display(self):
        print(f'{self.name} is {self.age} years old')

p = Person('kai',20)
p.display()
print(p.age)                

#-----protected--------(convention not really enforced)
class Person2:
    def __init__(self,name,age):
        self.name = name
        self._age = age 

    def display(self):
        print(f'{self.name} is {self._age} years old')

p2 = Person2('alice',32) 
p2.display()       
print(p2._age)

#--------private--------

class Person3:
    def __init__(self,name,age):
        self.name = name
        self.__age = age 

    def display(self):
        print(f'{self.name} is {self.__age} years old')

p3 = Person3('alice',33) 
p3.display()  
#print(p3.__age)
# Private attributes can still be accessed using name mangling (not recommended)
print(p3._Person3__age)  # Output: 25     

