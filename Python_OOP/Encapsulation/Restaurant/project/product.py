class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value





