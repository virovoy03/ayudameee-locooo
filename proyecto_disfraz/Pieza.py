
class Disfraz:
    def __init__(self,descripcion,talle,precio,estado,id):
        self.descripcion = descripcion
        self.talle = talle
        self.precio = precio
        self.estado = estado
        self.id = id

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre
