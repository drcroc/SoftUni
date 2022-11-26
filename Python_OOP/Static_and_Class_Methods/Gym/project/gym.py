from project.customer import Customer
from project.equipment import Equipment
from project.subscription import Subscription
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def __get_customer(self, id):
        return [x for x in self.customers if x.id == id][0]

    def __get_trainer(self, id):
        return [x for x in self.trainers if x.id == id][0]

    def __get_equipment(self, id):
        return [x for x in self.equipment if x.id == id][0]

    def __get_plan(self, id):
        return [x for x in self.plans if x.id == id][0]

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ''
        for x in self.subscriptions:
            if x.id == subscription_id:
                customer = self.__get_customer(x.customer_id)
                trainer = self.__get_trainer(x.trainer_id)
                plan = self.__get_plan(x.customer_id)
                equipment = self.__get_equipment(plan.equipment_id)
                result += f'{x}\n{customer}\n{trainer}\n{equipment}\n{plan}'

        return result