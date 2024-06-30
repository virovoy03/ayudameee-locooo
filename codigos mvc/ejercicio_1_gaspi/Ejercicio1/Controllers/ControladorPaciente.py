
from Models.Paciente import Paciente
from Views.VistaPaciente import VistaPaciente

class ControladorPaciente:
    def __init__(self):
        self.vista = VistaPaciente()
        self.modelo = Paciente()
        self.listaPacientes = []

    def cargarArchivo(self):
        with open("Scripts\\pacientes.txt") as f:
            renglones = f.readlines()
        for r in renglones:
            nombre, codigo = r.strip().split(",")
            self.listaPacientes.append(Paciente(nombre, codigo))
        self.vista.mostrar(self.listaPacientes)

    def getPaciente(self):
        self.vista.mostrar(self.listaPacientes)
        codigo = self.vista.getCodigo()
        return self.buscarObjeto(codigo)

    def buscarObjeto(self, codigo):
        for i in self.listaPacientes:
            if i.codigo == codigo:
                return i

    def iniciar(self):
        self.cargarArchivo()
