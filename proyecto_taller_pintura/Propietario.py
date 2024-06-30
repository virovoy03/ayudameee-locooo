
class Propietario:
    def __init__(self,codigo,nombre,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return str(self.codigo)+"-"+self.nombre

    def __repr__(self):
        return self.nombre
