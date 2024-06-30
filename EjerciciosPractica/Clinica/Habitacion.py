class Habitacion:
    def __init__(self, numero, enfermera, ubicacion, camas, estado="habilitada", ocupacion=0):
        self.numero = numero
        self.enfermera = enfermera
        self.ubicacion = ubicacion
        self.camas = camas
        self.estado = estado
        self.ocupacion = ocupacion


    def camas_disponibles(self):
        return self.camas - self.ocupacion


    def registrar_paciente(self):
        if self.camas_disponibles() > 0:
            self.ocupacion += 1
            print(f"Cama asiganda en la habitación {self.numero}.")
        else:
            print(f"No hay camas disponibles en la habitación {self.numero}.")

    def sacar_paciente(self):
        if self.camas_disponibles() != 0:
            self.ocupacion -= 1
            print(f"Cama libre en la habitación {self.numero}.")
        else:
            print(f"Todas las camas estan liberadas en la habitación {self.numero}.")
