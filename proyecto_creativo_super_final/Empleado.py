
class Empleado:
    def __init__(self,nombre,dni,telefono,contraseña,estado):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.contraseña = contraseña
        self.estado = estado
        
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre