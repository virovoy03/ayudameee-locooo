
class Cliente:
    def __init__(self,nombre,dni,telefono,mail,estado):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.mail = mail
        self.reclamos = []
        self.estado = estado

    def is_habilitado(self):
        if self.estado == "1":
            return "Habilitado"
        return "No habilitado"
    
    def __str__(self):
        return f"El cliente: {self.nombre} con dni: {self.dni} {self.telefono} {self.mail}"
    
    def __repr__(self):
        return f"El cliente: {self.nombre} con dni: {self.dni} {self.telefono} {self.mail}"