
from Modelos.Habitacion import Habitacion
from Vistas.Vista_Habitacion import Vista_Habitacion



class Controlador_habitacion:
    def __init__(self):
        self.vista = Vista_Habitacion()
        self.lista_habitaciones = []
    
    def iniciar(self):
        self.cargar_archivo()
        self.vista.mostrar(self.lista_habitaciones)
    
    def cargar_archivo(self):
        with open("habitaciones.txt") as archivo:
            renglones = archivo.readlines()
        for linea in renglones:
            estado,numero_de_habitacion,ocupacion,cantidad_de_camas = linea.strip().split(",")
            self.lista_habitaciones.append(Habitacion(estado,numero_de_habitacion,ocupacion,cantidad_de_camas))
    
    def listar_camas_disponibles(self):
        pass