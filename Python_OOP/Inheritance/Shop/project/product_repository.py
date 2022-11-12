from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.__class__.__name__:
                return product

    def remove(self, product_name: str):
        for x in self.products:
            if product_name == x.name:
                self.products.remove(x)

    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f'{product}: {product.quantity}')

        return '\n'.join(output)
