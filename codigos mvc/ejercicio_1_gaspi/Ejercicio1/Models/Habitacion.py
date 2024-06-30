
class Habitacion:
    def __init__(self, estado="", numero="", ocupacion="", camas=""):
        self.estado = estado
        self.numero = numero
        self.ocupacion = ocupacion
        self.camas = camas
        self.pacientes = []

    def estadoS(self):
        if self.estado == "1":
            return "Habilitado"
        return "deshabilitado"

    def camasDisponibles(self):
        if self.camas > self.ocupacion and self.estado==1:
            return True
        return False

    def __str__(self):
        return f'{self.numero} - {self.estadoS()}'

    def __repr__(self):
       return f'{self.numero} - {self.estadoS()}'
