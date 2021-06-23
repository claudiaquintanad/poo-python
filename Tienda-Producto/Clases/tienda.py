class Tienda:
    def __init__(self, name, listaproductos):
        self.name = name
        self.listaproductos = []
    def add_product (self, new_product):
        self.listaproductos.append(new_product)
    def sell_product (self, id):
        self.lista_de_productos.remove(id)
    

