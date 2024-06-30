
class Producto:
    def __init__(self,nombre="",precio=0.0,cantidad_disponible=0,cantidad_vendida=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.cantidad_vendida = cantidad_vendida
    
    def __repr__(self):
        return self.nombre

    def __str__(self):
        return f"el articulo es: {self.nombre} y su precio es: {self.precio}"
    
        
        
    
        
        
