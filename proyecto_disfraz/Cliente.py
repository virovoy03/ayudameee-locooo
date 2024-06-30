
class Cliente:
    def __init__(self,nombre,telefono,mail,dni,estado):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail
        self.dni = dni
        self.estado = estado

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre