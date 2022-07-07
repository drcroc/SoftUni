class Catalogue:
    catalogue = []
    filtered = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name: str):
        self.catalogue.append(product_name)

    def get_by_letter(self, first_letter: str):
        for name in self.catalogue:
            if name[0] == first_letter:
                self.filtered.append(name)

        return self.filtered

    def __str__(self):
        self.catalogue.sort()
        print(f'Items in the {self.name} catalogue:')
        return '\n'.join(self.catalogue)


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)



