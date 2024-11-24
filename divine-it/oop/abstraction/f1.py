from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


#  so shape is the abstact class while perimeter and area are abstract method (implemented by subclasses)
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print('the mileage is 30 km/h')

class Suzuki(Car):
    def mileage(self):
        print('the mileage is 20 km/h')

t = Tesla()
t.mileage()                    