from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @property
    def delicacy_menu(self):
        return {
            "Stolen": Stolen,
            "Gingerbread": Gingerbread
        }

    @property
    def booth_property(self):
        return {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth
        }

    def __find_empty_booth(self, num):
        for booth in self.booths:
            if booth.capacity >= num and not booth.is_reserved:
                return booth

    def __find_booth(self, num):
        for booth in self.booths:
            if booth.booth_number == num:
                return booth

    def __find_delicacy(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if any(name == d.name for d in self.delicacies):
            raise Exception(f'{name} already exists!')

        if type_delicacy not in self.delicacy_menu:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        self.delicacies.append(self.delicacy_menu[type_delicacy](name, price))
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if any(booth_number == b.booth_number for b in self.booths):
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth not in self.booth_property:
            raise Exception(f'{type_booth} is not a valid booth!')

        self.booths.append(self.booth_property[type_booth](booth_number, capacity))
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_empty_booth(number_of_people)

        if booth is None:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if not self.__find_delicacy(delicacy_name):
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        if not self.__find_booth(booth_number):
            raise Exception(f"Could not find booth {booth_number}!")

        booth = self.__find_booth(booth_number)
        delicacy = self.__find_delicacy(delicacy_name)

        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        food_cost = 0
        booth = self.__find_booth(booth_number)

        for food in booth.delicacy_orders:
            food_cost += food.price

        bill = booth.price_for_reservation + food_cost
        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'
