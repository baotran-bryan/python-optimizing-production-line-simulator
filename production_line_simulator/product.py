class Product:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Product {self.id}"
