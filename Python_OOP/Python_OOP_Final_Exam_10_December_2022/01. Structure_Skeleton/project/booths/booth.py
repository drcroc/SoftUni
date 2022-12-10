from abc import ABC, abstractmethod


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        self.capacity = capacity
        self.booth_number = booth_number
        self.delicacy_orders = []
        self.price_for_reservation = float()
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError('Capacity cannot be a negative number!')

        self.__capacity = value

    def reserve(self, number_of_people: int):
        pass


