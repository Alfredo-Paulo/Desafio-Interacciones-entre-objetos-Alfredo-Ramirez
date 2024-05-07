class Producto():
    def __init__(self, nombre: str, precio: int, stock:int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    
    @property
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_precio(self):
        return self.__precio
    
    @property
    def get_stock(self):
        return self.__stock
    
    @get_stock.setter
    def mod_stock(self, cantidad):
        if cantidad <= 0:
            cantidad = 0
        self.__stock += cantidad