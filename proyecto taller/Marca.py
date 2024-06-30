
class Marca:
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"{self.codigo},{self.nombre}"

    def __repr__(self):
        return f"{self.codigo},{self.nombre}"
