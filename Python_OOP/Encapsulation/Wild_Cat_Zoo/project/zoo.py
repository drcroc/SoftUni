from project.worker import Worker
from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if price > self.__budget:
                return f'Not enough budget'

            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        return f'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return f'Not enough space for worker'

    def fire_worker(self, worker):
        for pos, w in enumerate(self.workers):
            if worker == w.name:
                del self.workers[pos]
                return f'{worker} fired successfully'

        return f'There is no {worker} in the zoo'

    def pay_workers(self):
        workers_salary = 0
        for worker in self.workers:
            workers_salary += worker.salary

        # if 0 <= self.__budget - workers_salary:
        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_expenses = 0
        for animal in self.animals:
            animal_expenses += animal.money_for_care

        if 0 <= self.__budget - animal_expenses:
            self.__budget -= animal_expenses
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        info = {"Cheetah": [], "Tiger": [], "Lion": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]

        output = [f"You have {len(self.animals)} animals",
                  f"----- {len(info['Lion'])} Lions:", *info['Lion'],
                  f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
                  f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]

        return "\n".join(output)

    def workers_status(self):
        info = {"Keeper": [], "Vet": [], "Caretaker": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]
        output = [f"You have {len(self.workers)} workers",
                  f"----- {len(info['Keeper'])} Keepers:", *info['Keeper'],
                  f"----- {len(info['Caretaker'])} Caretakers:", *info['Caretaker'],
                  f"----- {len(info['Vet'])} Vets:", *info['Vet']]
        return "\n".join(output)
