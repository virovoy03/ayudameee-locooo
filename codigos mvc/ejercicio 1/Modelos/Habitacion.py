
class Habitacion:
    def __init__(self,estado,numero_de_habitacion,ocupacion,cantidad_de_camas):
        self.estado = int(estado)
        self.numero_de_habitacion = numero_de_habitacion
        self.ocupacion = int(ocupacion)
        self.cantidad_de_camas = int(cantidad_de_camas)

    def estados(self):
        if self.estado == 1:
            return "habilitado"
        elif self.estado == 0:
            return "deshabilitado" 
        
    def camas_disponibles(self):
        if self.ocupacion < self.cantidad_de_camas:
            return True 
        else:
            return False
        
    def __str__(self):
        return f'{self.numero_de_habitacion} - {self.estados()}'
    
    def __repr__(self):
        return f'{self.numero_de_habitacion} - {self.estados()}'