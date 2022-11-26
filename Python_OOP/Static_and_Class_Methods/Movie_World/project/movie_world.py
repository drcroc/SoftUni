from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    # def __get_customer(self, id):
    #     return [customer for customer in self.customers if id == customer.id][0]
    #
    # def __get_dvd(self, id):
    #     return [x for x in self.dvds if x.id == id][0]

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:  # This can be its own function
            if customer.id == customer_id:  #

                for dvd in self.dvds:   # This can be its own function
                    if dvd.id == dvd_id:    #

                        if customer.age < dvd.age_restriction:
                            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

                        if dvd.is_rented:
                            if dvd in customer.rented_dvds:
                                return f'{customer.name} has already rented {dvd.name}'

                            return 'DVD is already rented'

                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:  # This can be its own function
            if customer.id == customer_id:  #

                for dvd in self.dvds:  # This can be its own function
                    if dvd.id == dvd_id:    #

                        if dvd in customer.rented_dvds:
                            customer.rented_dvds.remove(dvd)
                            dvd.is_rented = False
                            return f'{customer.name} has successfully returned {dvd.name}'

                        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        output = ""
        for x in self.customers:
            output += f"{str(x)}\n"
        for x in self.dvds:
            output += f"{str(x)}\n"
        return output.rstrip()
