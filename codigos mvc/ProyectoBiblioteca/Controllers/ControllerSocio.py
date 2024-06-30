from Views.ViewSocio import ViewSocio
from Models.Socio import Socio


class ControllerSocio:
    def __init__(self, vista=ViewSocio(), listaSocios=[], model=Socio()):
        self._vista = vista
        self._listaSocios = listaSocios
        self._model = model

    def cargarArchivos(self):
        with open("\\Archivos\\socios.txt", "r") as file:
            lineas = file.readlines()
        for i in lineas:
            codigo, nombre, apellido, estado = i.strip().split(",")
            self._listaSocios.append(Socio(codigo, nombre, apellido, estado))

    def listaSociosHabilitados(self):
        with open("\\Archivos\\socios.txt", "r") as file:
            linea = file.readlines().split(",").strip()
            self._listaSocios = []
        for socio in linea:
            if linea[3] == "1":
                self._listaSocios.append(socio)
            return self._listaSocios
        return None

    def mostrar(self):
        for i in self._listaSocios:
            pass
        self._vista.mostrar(self._listaSocios)

    def iniciar(self):
        self.cargarArchivos()
        self.mostrar()
