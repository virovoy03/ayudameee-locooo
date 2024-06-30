from Models.Materia import Materia
from View.VistaMateria import VistaMateria


class ControllerMateria:
    def __init__(self):
        self._vista = VistaMateria()
        self._modelo = Materia()
        self._listaMateriasCurricula = []

    def buscarMateria(self, codigo):
        for materia in self._listaMateriasCurricula:
            if int(materia.getCodigo()) == int(codigo):
                return materia
        return None

    def cargarMateriasDesdeArchivo(self):
        with open("MateriasCurricula.txt", "r") as file:
            for line in file.readlines():
                linea = line.split(",")
                materia = Materia(linea[0], linea[1])
                materia.setCorrelativas([])
                try:
                    if int(linea[2]) > 0:
                        materia.getCorrelativas().append(self.buscarMateria(linea[2]))
                except ValueError:
                    materia.setCorrelativas([])
                self._listaMateriasCurricula.append(materia)
        return self._listaMateriasCurricula

    def getListaMateriasCurricula(self):
        if self._listaMateriasCurricula == []:
            self.cargarMateriasDesdeArchivo()
        return self._listaMateriasCurricula

    def visualizarCorrelativas(self, materias):
        if len(materias) != 0:
            for mat in materias:
                self._vista.visualizarCorrelativa(mat)

    def mostrarDatos(self):
        self._vista.visualizarMateria(self._modelo)
