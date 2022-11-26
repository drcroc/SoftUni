from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance

    def refuel(self, amount):
        self.fuel_quantity += amount


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_consumption * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95
