from Models.Inscripcion import Inscripcion
from View.VistaInscripcion import VistaInscripcion
from Controller.ControllerMateria import ControllerMateria
from Controller.ControllerAlumno import ControllerAlumno


class ControllerInscripcion:
    def __init__(
        self,
    ):
        self._vista = VistaInscripcion()
        self._modelo = Inscripcion()
        self._controllerMateria = ControllerMateria()
        self._controllerAlumno = ControllerAlumno(self._controllerMateria)

    def mostrarListaMaterias(self):
        listaMaterias = self._controllerMateria.getListaMateriasCurricula()
        for materia in listaMaterias:
            self._controllerMateria._vista.visualizarMateria(materia)
            if materia.getCorrelativas() != []:
                self._controllerMateria.visualizarCorrelativas(
                    materia.getCorrelativas()
                )

    def getAlumnoFor(self, legajo):
        self._modelo.setAlumno(self._controllerAlumno.buscarAlumno(legajo))
        # self._vista.mostrarDato(self._modelo)
        self._controllerAlumno.mostrarDatos()

    def getMateriaFor(self, codigo):
        self._modelo.setMateria(self._controllerMateria.buscarMateria(codigo))
        self._vista.mostrarDato(self._modelo)

    def inscribir(self):
        self._modelo.inscribirAlumno()
        self._vista.mostrarDato(self._modelo)

    def registrarInscripcion(self):
        legajo = self._vista.getLegajoAlumno()
        self.getAlumnoFor(legajo)
        codigo = self._vista.getCodigoMateria()
        self.getMateriaFor(codigo)
        self.inscribir()

    def iniciar(self):
        self._vista.mostrarBienvenida()
        self.mostrarListaMaterias()
        self.registrarInscripcion()
