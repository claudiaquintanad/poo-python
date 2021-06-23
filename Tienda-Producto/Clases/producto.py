class Producto:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def print_info (self):
        print(f"Nombre del Producto: {self.name}, Categoria: {self.category}, Precio: {self.price}")
        return self
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        elif is_increased == False:
            self.price = self.price - (self.price * percent_change)
        return self
