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


#----getter & setter methods-----
class Person4:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #private attribute

    def get_age(self):
        return self.__age 

    def set_age(self, age):
        if age>0:
            self.__age = age
        else:
            print('age must be positive int')   

p4 = Person4('jev',23)
print(p4.get_age())
p4.set_age(30)            
print(p4.get_age())  


#-----using property instead of getter & setter-------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age must be positive")

p = Person("Alice", 25)
print(p.age)  # Output: 25 (Getter)

p.age = 30    # Setter
print(p.age)  # Output: 30

p.age = -5    # Invalid input
# Output: Age must be positive
