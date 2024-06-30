
class Paciente:
    def __init__(self, nombre="", codigo=""):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f'{self.nombre} - {self.codigo}'

    def __repr__(self):
        return f'{self.nombre} - {self.codigo}'
