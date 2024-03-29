from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    animal_food = {
        "Owl": {"food": ["Meat"], "add_weight": 0.25},
        "Hen": {"food": ["Vegetable", "Fruit", "Meat", "Seed"], "add_weight": 0.35},
        "Mouse": {"food": ["Vegetable", "Fruit"], "add_weight": 0.10},
        "Cat": {"food": ["Vegetable", "Meat"], "add_weight": 0.30},
        "Dog": {"food": ["Meat"], "add_weight": 0.40},
        "Tiger": {"food": ["Meat"], "add_weight": 1.00}
    }

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        animal_type = self.__class__.__name__
        food_type = food.__class__.__name__
        if food_type not in Animal.animal_food[animal_type]['food']:
            return f'{animal_type} does not eat {food_type}!'
        self.weight += food.quantity * Animal.animal_food[animal_type]['add_weight']
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'

