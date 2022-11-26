from math import log2, floor, ceil
from abc import ABC, abstractmethod


# processor: str, ram:int, price:int

class Computer(ABC):
    AVAILABLE_PROCESSORS = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError(f"Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError(f"Model name cannot be empty.")

        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @staticmethod
    def validating_ram(value):
        power = log2(value)
        return float(power) == ceil(power)

    def set_computer_parts(self, processor, ram):
        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSORS[processor] + int(log2(ram)) * 100

    def __repr__(self):
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'
