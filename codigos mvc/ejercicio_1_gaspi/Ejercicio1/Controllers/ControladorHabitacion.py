from Models.Habitacion import Habitacion
from Views.VistaHabitacion import VistaHabitacion
from Controllers.ControladorPaciente import ControladorPaciente


class ControladorHabitacion:
    def __init__(self, controladorPaciente):
        self.vista = VistaHabitacion()
        self.modelo = Habitacion()
        self.listaHabitaciones = []
        self.controladorPaciente = controladorPaciente

    def cargarArchivo(self):
        with open("Scripts\\habitaciones.txt") as f:
            renglones = f.readlines()
        for r in renglones:
            estado, numero, ocupacion, camas = r.strip().split(",")
            self.listaHabitaciones.append(Habitacion(estado, numero, ocupacion, camas))
        self.vista.mostrarLista(self.listaHabitaciones)

    def listarCamasDisponibles(self):
        lista2 = []
        for i in self.listaHabitaciones:
            if i.camasDisponibles():
                lista2.append(i)
        self.vista.mostrarHabitaciones(lista2)

    def buscarObjeto(self, numero):
        for i in self.listaHabitaciones:
            if i.numero == numero:
                return i

    def registrarPaciente(self):
        self.vista.mostrarLista(self.listarCamasDisponibles())
        numero = self.vista.getHabitacion()
        objH = self.buscarObjeto(numero)
        objP = self.controladorPaciente.getPaciente()
        objH.append(objP)

    def mostrarMenu(self):
        self.vista.mostrarMenu()
        op = self.vista.getOpcion()
        if op == "1":
            self.listarCamasDisponibles()
        if op == "2":
            self.vista.mostrarLista(self.listaHabitaciones)
        if op == "3":
            self.registrarPaciente()
        if op == "4":
            self.listarPacientesXHabitacion()

    def iniciar(self):
        self.cargarArchivo()
        self.vista.mostrarHabitaciones(self.listaHabitaciones)
        self.listarCamasDisponibles()
