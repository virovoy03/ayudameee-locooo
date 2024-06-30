from View.VistaAlumno import VistaAlumno
from Models.Alumno import Alumno
from Controller.ControllerMateria import ControllerMateria


class ControllerAlumno:
    def __init__(self, controladorMateria):
        self._vista = VistaAlumno()
        self._modelo = Alumno()
        self._controllerMateria = controladorMateria

    def buscarAlumno(self, legajo):
        with open("Alumnos.txt", "r") as file:
            for line in file.readlines():
                linea = line.split(",")
                if int(linea[0]) == int(legajo):
                    self._modelo = Alumno(linea[0], linea[1])
                    self._modelo.setAprobadas([])
                    try:
                        if int(linea[2]) > 0:
                            self._modelo.getAprobadas().append(
                                self._controllerMateria.buscarMateria(linea[2])
                            )
                    except ValueError:
                        self._modelo.setAprobadas([])
                    return self._modelo
        return None

    def mostrarDatos(self):
        self._vista.visualizarAlumno(self._modelo)
        self._vista.visualizarAprobadas(self._modelo.getAprobadas())
