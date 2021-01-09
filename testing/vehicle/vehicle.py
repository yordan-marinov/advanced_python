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
