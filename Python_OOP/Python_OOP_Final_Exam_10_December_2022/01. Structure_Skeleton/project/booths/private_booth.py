from project.booths.booth import Booth


class PrivateBooth(Booth):
    price_per_person = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        if self.capacity >= number_of_people and not self.is_reserved:
            self.price_for_reservation = self.price_per_person * number_of_people
            self.is_reserved = True



