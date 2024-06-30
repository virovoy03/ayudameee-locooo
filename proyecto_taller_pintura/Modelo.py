
class Modelo:
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return str(self.codigo)+"-"+self.nombre

    def __repr__(self):
        return self.nombre