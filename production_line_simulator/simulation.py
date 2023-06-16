from .product import Product


class ProductionLineSimulation:
    def __init__(self, layout):
        self.layout = layout

    def run_simulation(self, num_products):
        for i in range(num_products):
            product = Product(i)
            self.process_product(product)
        return range(num_products)

    def process_product(self, product):
        for workstation in self.layout:
            workstation.process_product(product)
