from random import randrange
class Producto:
    
    precio = 0
    nombre = ""
    
    def generarPrecio(self):
        self.precio = randrange (1000,9990)
