
class Pelicula:
    def __init__(self,nombre,precio,pelicula_sem,estado):
        self.nombre = nombre
        self.precio = precio
        self.pelicula_sem = pelicula_sem
        self.estado = estado
    
    def __repr__(self):
        return f"{self.nombre},{self.precio},{self.pelicula_sem},{self.estado}"
         
        
        
