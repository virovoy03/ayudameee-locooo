
from Vistas.Vista_Cliente import Vista_Cliente
from Modelos.Cliente import Cliente

class Controlador_Cliente:
    def __init__(self,vista=Vista_Cliente(),lista_clientes=[]):
        self.vista = vista
        self.lista_clientes = lista_clientes
             
    
    def cargar_archivos(self):
        with open("C:\\Users\\santiago\\Documents\\Santi\\general\\uni\\2do cuatrimestre\\laboratorio_2\\codigos mvc\\codigo libro ia mvc\\Archivos", "r") as file:
            lineas = file.readlines()
        for i in lineas:
            nombre,dni,telefono,mail,estado = i.strip().split(",")
            self.lista_clientes.append(Cliente(nombre,dni,telefono,mail,estado))

    def mostrar(self):
        for i in self.lista_clientes:
            return self.nombre
        
    def iniciar(self):
        self.cargar_archivos()
        self.mostrar()

        