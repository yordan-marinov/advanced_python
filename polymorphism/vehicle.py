from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption  # liters per km

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    @staticmethod
    def fuel_is_enough(available_liters, needed_liters):
        return available_liters >= needed_liters


class Car(Vehicle):
    summer_consumption = 0.9

    def drive(self, distance):
        self.fuel_consumption += Car.summer_consumption
        needed_quantity = distance * self.fuel_consumption
        if Vehicle.fuel_is_enough(self.fuel_quantity, needed_quantity):
            self.fuel_quantity -= needed_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    summer_consumption = 1.6

    def drive(self, distance):
        self.fuel_consumption += Truck.summer_consumption
        needed_quantity = distance * self.fuel_consumption
        if Vehicle.fuel_is_enough(self.fuel_quantity, needed_quantity):
            self.fuel_quantity -= needed_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


car = Car(10, 10)
truck = Truck(10, 10)
print(car.fuel_quantity)
print(car.fuel_consumption)
print(truck.fuel_quantity)
print(truck.fuel_consumption)
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
