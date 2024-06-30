from Models.Alumno import Alumno
from Models.Materia import Materia


class Inscripcion:
    def __init__(self, alumno="", materia="", estado=""):
        self._alumno = alumno
        self._materia = materia
        self._estado = estado

    def getAlumno(self):
        return self._alumno

    def getMateria(self):
        return self._materia

    def getEstado(self):
        return self._estado

    def getEstadoS(self):
        if self._estado == 0:
            return "Inscripto"
        elif self._estado == 1:
            return "No se puede inscribir por las correlativas"
        elif self._estado == 2:
            return "La materia ya fue aprobada"
        return " * "

    def setAlumno(self, dato):
        self._alumno = dato

    def setMateria(self, dato):
        self._materia = dato

    def setEstado(self, dato):

        self._estado = dato

    def __str__(self):
        return (
            str(self.getAlumno())
            + " - "
            + str(self.getMateria())
            + " - "
            + str(self.getEstadoS())
        )

    def inscribirAlumno(self):
        if isinstance(self._alumno, Alumno) and isinstance(self._materia, Materia):
            if self._materia in self._alumno.getAprobadas():
                self.setEstado(2)
            else:
                self.setEstado(
                    self._materia.isPosibleInscribirse(self._alumno.getAprobadas())
                )
