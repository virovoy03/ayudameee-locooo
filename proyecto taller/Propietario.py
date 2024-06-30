
class Propietario:
    def __init__(self,codigo,nombre,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre}, Telefono: {self.telefono}"

    def __repr__(self):
        return f"{self.nombre}, Telefono: {self.telefono}"

