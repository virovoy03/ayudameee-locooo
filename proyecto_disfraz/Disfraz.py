
class Disfraz:
    def __init__(self,categoria,nombre,estado,id):
        self.categoria = categoria
        self.nombre = nombre
        self.estado = estado
        self.id = id

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre
