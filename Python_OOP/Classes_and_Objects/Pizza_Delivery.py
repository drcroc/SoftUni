class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            if self.ingredients.get(ingredient) >= quantity:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_quantity * quantity
            else:
                return f'Please check again the desired quantity of {ingredient}!'
        else:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

    def make_order(self):
        self.ordered = True

        ingredient = ''
        for keys, values in self.ingredients.items():
            ingredient += f'{keys}: {values}, '

        return f"You've ordered pizza {self.name} prepared with {ingredient[:-2]}" \
               f" and the price will be {self.price}lv."

