class Car:
    total_cars = 0

    def __init__(self, model, make) -> None:
        self.model = model
        self.make = make
        Car.total_cars += 1

    # instance method
    def display(self):
        return f"Car: {self.make} {self.model}"

    # class method
    @classmethod
    def display_total_cars(cls):
        return f"total cars {cls.total_cars}"

    # static method
    @staticmethod
    def is_valid_car_type(car_type):
        valid_types = ["SUV", "Sedan", "Hatchback"]
        return car_type in valid_types


car1 = Car("Toyota", "Corolla")

print(car1.display())  # Car: Toyota Corolla
print(Car.display_total_cars())  # Total cars: 2
print(Car.is_valid_car_type("SUV"))
