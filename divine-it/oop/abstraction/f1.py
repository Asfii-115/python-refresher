from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


#  so shape is the abstact class while perimeter and area are abstract method (implemented by subclasses)
